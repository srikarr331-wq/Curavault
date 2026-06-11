# Database Schema

## Overview

CuraVault uses PostgreSQL as the primary database with the following tables:

## Tables

### users

Stores user account information.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | UUID | PK | User ID |
| email | VARCHAR(255) | UNIQUE, NOT NULL | User email |
| full_name | VARCHAR(255) | NOT NULL | Full name |
| password_hash | VARCHAR(255) | NOT NULL | Hashed password |
| phone | VARCHAR(20) | | Phone number |
| role | ENUM | NOT NULL, DEFAULT='patient' | User role |
| is_active | BOOLEAN | DEFAULT=false | Account active status |
| is_verified | BOOLEAN | DEFAULT=false | Email verified status |
| email_verified_at | TIMESTAMP | | Email verification time |
| last_login | TIMESTAMP | | Last login time |
| last_login_ip | VARCHAR(45) | | Last login IP address |
| mfa_enabled | BOOLEAN | DEFAULT=false | MFA enabled |
| mfa_secret | VARCHAR(255) | | MFA secret key |
| created_at | TIMESTAMP | DEFAULT=NOW() | Creation time |
| updated_at | TIMESTAMP | DEFAULT=NOW() | Update time |

**Indexes:**
- UNIQUE INDEX idx_users_email (email)
- INDEX idx_users_role (role)
- INDEX idx_users_created_at (created_at)

---

### doctors

Stores doctor information.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | UUID | PK | Doctor ID |
| user_id | UUID | FK users(id), UNIQUE | Reference to user |
| license_number | VARCHAR(50) | UNIQUE, NOT NULL | Medical license number |
| specialization | VARCHAR(255) | | Medical specialization |
| hospital_id | UUID | FK hospitals(id) | Associated hospital |
| bio | VARCHAR(1000) | | Professional bio |
| profile_image_url | VARCHAR(500) | | Profile image URL |
| created_at | TIMESTAMP | DEFAULT=NOW() | Creation time |
| updated_at | TIMESTAMP | DEFAULT=NOW() | Update time |

**Indexes:**
- UNIQUE INDEX idx_doctors_user_id (user_id)
- UNIQUE INDEX idx_doctors_license (license_number)
- INDEX idx_doctors_hospital_id (hospital_id)

---

### hospitals

Stores hospital/organization information.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | UUID | PK | Hospital ID |
| name | VARCHAR(255) | UNIQUE, NOT NULL | Hospital name |
| address | VARCHAR(500) | NOT NULL | Street address |
| city | VARCHAR(100) | NOT NULL | City |
| state | VARCHAR(100) | NOT NULL | State/Province |
| pincode | VARCHAR(10) | NOT NULL | Postal code |
| phone | VARCHAR(20) | NOT NULL | Contact phone |
| email | VARCHAR(255) | NOT NULL | Contact email |
| website | VARCHAR(255) | | Hospital website |
| logo_url | VARCHAR(500) | | Hospital logo URL |
| created_at | TIMESTAMP | DEFAULT=NOW() | Creation time |
| updated_at | TIMESTAMP | DEFAULT=NOW() | Update time |

**Indexes:**
- UNIQUE INDEX idx_hospitals_name (name)
- INDEX idx_hospitals_city (city)

---

### reports

Stores medical reports/documents.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | UUID | PK | Report ID |
| user_id | UUID | FK users(id), NOT NULL | Report owner |
| title | VARCHAR(255) | NOT NULL | Report title |
| description | TEXT | | Report description |
| report_type | ENUM | NOT NULL | Type of report |
| file_url | VARCHAR(500) | NOT NULL | S3 file URL |
| file_size | INTEGER | NOT NULL | File size in bytes |
| mime_type | VARCHAR(50) | NOT NULL | File MIME type |
| test_date | VARCHAR(50) | | Date of test |
| doctor_name | VARCHAR(255) | | Attending doctor |
| lab_name | VARCHAR(255) | | Lab name |
| extracted_text | TEXT | | OCR extracted text |
| ai_summary | TEXT | | AI generated summary |
| created_at | TIMESTAMP | DEFAULT=NOW() | Creation time |
| updated_at | TIMESTAMP | DEFAULT=NOW() | Update time |

**Indexes:**
- INDEX idx_reports_user_id (user_id)
- INDEX idx_reports_report_type (report_type)
- INDEX idx_reports_test_date (test_date)
- INDEX idx_reports_created_at (created_at)

---

### prescriptions

Stores prescription information.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | UUID | PK | Prescription ID |
| user_id | UUID | FK users(id), NOT NULL | Patient |
| doctor_id | UUID | FK doctors(id) | Prescribing doctor |
| medicine_name | VARCHAR(255) | NOT NULL | Medicine name |
| dosage | VARCHAR(100) | NOT NULL | Dosage |
| frequency | VARCHAR(100) | NOT NULL | Frequency |
| duration | VARCHAR(100) | NOT NULL | Duration |
| notes | TEXT | | Additional notes |
| file_url | VARCHAR(500) | | Prescription file URL |
| is_active | BOOLEAN | DEFAULT=true | Active status |
| created_at | TIMESTAMP | DEFAULT=NOW() | Creation time |
| updated_at | TIMESTAMP | DEFAULT=NOW() | Update time |

**Indexes:**
- INDEX idx_prescriptions_user_id (user_id)
- INDEX idx_prescriptions_doctor_id (doctor_id)
- INDEX idx_prescriptions_is_active (is_active)

---

### audit_logs

Stores activity audit logs.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | UUID | PK | Log ID |
| user_id | UUID | FK users(id) | User performing action |
| action | ENUM | NOT NULL | Action type |
| resource_type | VARCHAR(100) | | Resource type |
| resource_id | VARCHAR(36) | | Resource ID |
| ip_address | VARCHAR(45) | NOT NULL | Client IP address |
| user_agent | VARCHAR(500) | | Browser user agent |
| details | TEXT | | Additional details |
| created_at | TIMESTAMP | DEFAULT=NOW() | Log time |
| updated_at | TIMESTAMP | DEFAULT=NOW() | Update time |

**Indexes:**
- INDEX idx_audit_logs_user_id (user_id)
- INDEX idx_audit_logs_action (action)
- INDEX idx_audit_logs_resource_id (resource_id)
- INDEX idx_audit_logs_created_at (created_at)

---

## Relationships

```
users (1) ──→ (many) reports
users (1) ──→ (1) doctors
users (1) ──→ (many) prescriptions
users (1) ──→ (many) audit_logs
doctors (many) ──→ (1) hospitals
doctors (many) ──→ (many) prescriptions
```

---

## Performance Considerations

1. **Partitioning**: Audit logs can be partitioned by date for large datasets
2. **Archival**: Old reports (>5 years) can be archived to cold storage
3. **Indexing**: Composite indexes on frequently filtered columns
4. **Caching**: User profile data cached in Redis
5. **Search**: Full-text search on reports via Elasticsearch

---

## Migrations

Database migrations are managed using Alembic:

```bash
# Create migration
alembic revision --autogenerate -m "description"

# Apply migrations
alembic upgrade head

# Rollback
alembic downgrade -1
```
