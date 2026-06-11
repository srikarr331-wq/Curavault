# Security Implementation Guide

## 1. Authentication

### JWT Tokens

- **Algorithm**: HS256 (HMAC with SHA-256)
- **Access Token Lifetime**: 30 minutes
- **Refresh Token Lifetime**: 7 days
- **Token Storage**: httpOnly cookies (recommended for production)

**Token Claims:**
```json
{
  "sub": "user_id",
  "email": "user@example.com",
  "role": "patient",
  "iat": 1704110400,
  "exp": 1704112200
}
```

### Password Security

- **Algorithm**: bcrypt with salt rounds: 12
- **Minimum Length**: 8 characters
- **Requirements**:
  - At least one uppercase letter
  - At least one lowercase letter
  - At least one digit
  - At least one special character

---

## 2. Encryption

### Data at Rest

**Sensitive Fields Encrypted:**
- Patient phone numbers
- Medical history notes
- Prescription details
- Emergency contact information

**Encryption Algorithm:**
- AES-256-GCM (Galois/Counter Mode)
- Key Derivation: PBKDF2

```python
from cryptography.fernet import Fernet

cipher_suite = Fernet(encryption_key)
encrypted_data = cipher_suite.encrypt(sensitive_data.encode())
```

### Data in Transit

- **Protocol**: TLS 1.3 (minimum)
- **Certificate**: Let's Encrypt (production)
- **Cipher Suites**: Modern, forward-secret algorithms

---

## 3. Authorization

### Role-Based Access Control (RBAC)

**Roles:**
1. **Patient**: Access own records, share with doctors
2. **Doctor**: Access authorized patient records, create prescriptions
3. **Hospital Admin**: Manage doctors, view analytics
4. **System Admin**: Full platform access

**Permission Matrix:**

| Action | Patient | Doctor | Hospital Admin | System Admin |
|--------|---------|--------|----------------|-------------|
| View own records | ✓ | | | |
| Upload records | ✓ | | | |
| Share records | ✓ | | | |
| View shared records | ✓ | ✓ | | |
| Create prescription | | ✓ | | |
| Manage hospital | | | ✓ | |
| View audit logs | | | ✓ | ✓ |
| Manage users | | | | ✓ |
| System settings | | | | ✓ |

**Implementation:**
```python
from fastapi import Depends, HTTPException
from app.security.rbac import check_permission

@app.get("/api/v1/reports")
async def list_reports(current_user: User = Depends(get_current_user)):
    if not check_permission(current_user, "view_reports"):
        raise HTTPException(status_code=403, detail="Access denied")
    # Process request
```

---

## 4. API Security

### Rate Limiting

- **Default Limit**: 100 requests per hour per user
- **Burst Limit**: 10 requests per minute
- **Implementation**: Redis-based sliding window counter

```python
from slowapi import Limiter
from slowapi.util import get_remote_address

limiter = Limiter(
    key_func=get_remote_address,
    default_limits=["100/hour"],
)

@app.get("/api/v1/reports")
@limiter.limit("10/minute")
async def list_reports():
    pass
```

### CSRF Protection

- **Token-based CSRF**: Double-submit cookies
- **SameSite Attribute**: Strict (production)

```python
from fastapi_csrf_protect import CsrfProtect

@app.post("/api/v1/reports/upload")
async def upload_report(csrf_protect: CsrfProtect = Depends()):
    await csrf_protect.validate_csrf(request)
```

### Validation & Input Sanitization

- **Pydantic Schemas**: All inputs validated with type hints
- **Length Limits**: Maximum field lengths enforced
- **Pattern Matching**: Regex validation for emails, phones
- **SQL Injection Prevention**: SQLAlchemy parameterized queries
- **XSS Prevention**: HTML escaping, Content Security Policy

```python
from pydantic import BaseModel, EmailStr, Field

class ReportCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=255)
    description: str = Field(None, max_length=5000)
    report_type: str = Field(..., regex="^[a-z_]+$")
```

---

## 5. File Upload Security

### File Validation

- **Allowed Types**: PDF, JPEG, PNG (whitelist approach)
- **Max Size**: 50 MB per file
- **Virus Scanning**: ClamAV integration (optional)

```python
ALLOWED_MIME_TYPES = {
    "application/pdf": ".pdf",
    "image/jpeg": ".jpg",
    "image/png": ".png",
}

async def validate_upload(file: UploadFile):
    if file.content_type not in ALLOWED_MIME_TYPES:
        raise HTTPException(status_code=400, detail="Invalid file type")
    
    content = await file.read()
    if len(content) > 50 * 1024 * 1024:
        raise HTTPException(status_code=400, detail="File too large")
```

### Secure Storage

- **AWS S3**: Encrypted at rest (SSE-S3), private access
- **File Naming**: UUIDs to prevent directory traversal
- **Access Control**: Presigned URLs with 1-hour expiry

```python
import boto3
from datetime import datetime, timedelta

s3_client = boto3.client('s3')

# Generate presigned URL
url = s3_client.generate_presigned_url(
    'get_object',
    Params={'Bucket': bucket, 'Key': key},
    ExpiresIn=3600  # 1 hour
)
```

---

## 6. Audit & Logging

### Audit Log Events

All sensitive operations are logged:
- User login/logout
- Record uploads/downloads
- Data access by doctors
- Permission changes
- Administrative actions

```python
from app.models import AuditLog

async def log_action(
    user_id: str,
    action: str,
    resource_type: str,
    resource_id: str,
    ip_address: str,
    details: dict = None
):
    log = AuditLog(
        user_id=user_id,
        action=action,
        resource_type=resource_type,
        resource_id=resource_id,
        ip_address=ip_address,
        details=json.dumps(details) if details else None,
    )
    db.add(log)
    await db.commit()
```

### Logging Standards

- **Level**: INFO (normal), WARN (suspicious), ERROR (failures)
- **Format**: JSON for easy parsing
- **Retention**: 90 days in database, archive to S3
- **Monitoring**: Real-time alerts for security events

---

## 7. Data Privacy

### HIPAA Compliance (Healthcare)

- **PHI Protection**: Encryption and access controls
- **Audit Trails**: Complete activity logs
- **Data Breach**: 60-day notification requirement
- **Patient Rights**: Access, correction, deletion

### Data Minimization

- Only collect necessary data
- Regular deletion of obsolete data
- Data retention policies enforced

### User Consent

- Explicit consent for data sharing
- Granular permission controls
- Revocation anytime

---

## 8. Infrastructure Security

### Network Security

- **VPC**: Private subnets for databases
- **Security Groups**: Port restrictions (80, 443, 5432, 6379)
- **WAF**: Web Application Firewall (optional)
- **DDoS Protection**: AWS Shield Standard

### Container Security

- **Image Scanning**: Trivy for vulnerabilities
- **No Root**: Non-root user in containers
- **Secrets Management**: AWS Secrets Manager

### Secrets Management

```bash
# Using AWS Secrets Manager
aws secretsmanager create-secret \
  --name curavault/prod/db-password \
  --secret-string "password"
```

---

## 9. Security Headers

**CORS Headers:**
```
Access-Control-Allow-Origin: https://app.curavault.io
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, PUT, DELETE
Access-Control-Max-Age: 3600
```

**Security Headers:**
```
Strict-Transport-Security: max-age=31536000; includeSubDomains
X-Content-Type-Options: nosniff
X-Frame-Options: DENY
X-XSS-Protection: 1; mode=block
Content-Security-Policy: default-src 'self'; script-src 'self' 'unsafe-inline'
```

---

## 10. Security Checklist

- [ ] All endpoints require authentication (except public)
- [ ] All inputs validated with Pydantic schemas
- [ ] All sensitive data encrypted at rest
- [ ] TLS 1.3 enabled for all connections
- [ ] Rate limiting configured
- [ ] CSRF tokens implemented
- [ ] Audit logs for all sensitive operations
- [ ] File uploads validated and scanned
- [ ] Secrets in environment variables (not committed)
- [ ] Regular security audits scheduled
- [ ] Dependency vulnerabilities checked (Dependabot)
- [ ] SQL injection prevention (parameterized queries)
- [ ] XSS prevention (input escaping, CSP)

---

## 11. Incident Response

### Security Incident Procedure

1. **Detection**: Automated alerts from logs
2. **Containment**: Disable affected accounts/access
3. **Investigation**: Root cause analysis
4. **Notification**: Affected users notified (if data breach)
5. **Recovery**: Data restoration, system hardening
6. **Documentation**: Incident report filed

---

## 12. Compliance

- **HIPAA**: Healthcare compliance
- **GDPR**: European data protection
- **CCPA**: California privacy law
- **SOC 2**: Type II audit

---

## References

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [HIPAA Security Rule](https://www.hhs.gov/hipaa/for-professionals/security/laws-regulations/)
- [FastAPI Security](https://fastapi.tiangolo.com/tutorial/security/)
- [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework)
