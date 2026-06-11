# CuraVault - API Documentation

## Base URL

```
http://localhost:8000/api/v1
```

## Authentication

All protected endpoints require a Bearer token in the Authorization header:

```
Authorization: Bearer <access_token>
```

## Authentication Endpoints

### Register User

**POST** `/auth/register`

Create a new user account.

**Request Body:**
```json
{
  "email": "user@example.com",
  "full_name": "John Doe",
  "password": "SecurePass123",
  "confirm_password": "SecurePass123",
  "phone": "+1234567890"
}
```

**Response (201):**
```json
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "email": "user@example.com",
  "full_name": "John Doe",
  "role": "patient",
  "is_active": false,
  "is_verified": false,
  "created_at": "2024-01-01T12:00:00Z",
  "updated_at": "2024-01-01T12:00:00Z"
}
```

---

### Login

**POST** `/auth/login`

Authenticate user and get access tokens.

**Request Body:**
```json
{
  "email": "user@example.com",
  "password": "SecurePass123"
}
```

**Response (200):**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer",
  "expires_in": 1800
}
```

---

### Logout

**POST** `/auth/logout`

Invalidate current session.

**Response (200):**
```json
{
  "message": "Logout successful"
}
```

---

### Refresh Token

**POST** `/auth/refresh-token`

Get a new access token using refresh token.

**Response (200):**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer",
  "expires_in": 1800
}
```

---

### Forgot Password

**POST** `/auth/forgot-password`

Request password reset link.

**Query Parameters:**
- `email` (string, required): User email

**Response (200):**
```json
{
  "message": "Password reset link sent to email"
}
```

---

### Verify OTP

**POST** `/auth/verify-otp`

Verify one-time password.

**Query Parameters:**
- `email` (string, required): User email
- `otp` (string, required): One-time password

**Response (200):**
```json
{
  "message": "OTP verified"
}
```

---

## Medical Records Endpoints

### Upload Report

**POST** `/reports/upload`

Upload a medical report file.

**Request (multipart/form-data):**
- `file` (file, required): PDF or image file
- `title` (string, required): Report title
- `report_type` (string, required): Type of report
- `description` (string, optional): Report description
- `test_date` (string, optional): Test date
- `doctor_name` (string, optional): Doctor name

**Response (201):**
```json
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "user_id": "550e8400-e29b-41d4-a716-446655440001",
  "title": "Blood Test Report",
  "report_type": "blood_test",
  "file_url": "https://s3.amazonaws.com/...",
  "file_size": 1024000,
  "mime_type": "application/pdf",
  "created_at": "2024-01-01T12:00:00Z",
  "updated_at": "2024-01-01T12:00:00Z"
}
```

---

### List Reports

**GET** `/reports`

Get user's medical reports.

**Query Parameters:**
- `skip` (integer, default: 0): Number of records to skip
- `limit` (integer, default: 10): Number of records to return
- `report_type` (string, optional): Filter by report type

**Response (200):**
```json
[
  {
    "id": "550e8400-e29b-41d4-a716-446655440000",
    "user_id": "550e8400-e29b-41d4-a716-446655440001",
    "title": "Blood Test Report",
    "report_type": "blood_test",
    "file_url": "https://s3.amazonaws.com/...",
    "created_at": "2024-01-01T12:00:00Z",
    "updated_at": "2024-01-01T12:00:00Z"
  }
]
```

---

### Get Report

**GET** `/reports/{report_id}`

Get specific report details.

**Response (200):**
```json
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "user_id": "550e8400-e29b-41d4-a716-446655440001",
  "title": "Blood Test Report",
  "description": "Routine blood work",
  "report_type": "blood_test",
  "test_date": "2024-01-01",
  "doctor_name": "Dr. Smith",
  "file_url": "https://s3.amazonaws.com/...",
  "file_size": 1024000,
  "mime_type": "application/pdf",
  "extracted_text": "...",
  "ai_summary": "...",
  "created_at": "2024-01-01T12:00:00Z",
  "updated_at": "2024-01-01T12:00:00Z"
}
```

---

### Update Report

**PUT** `/reports/{report_id}`

Update report metadata.

**Request Body:**
```json
{
  "title": "Updated Title",
  "description": "Updated description",
  "doctor_name": "Dr. Jane"
}
```

**Response (200):**
Same as Get Report response

---

### Delete Report

**DELETE** `/reports/{report_id}`

Delete a medical report.

**Response (200):**
```json
{
  "message": "Report deleted successfully"
}
```

---

### Download Report

**GET** `/reports/{report_id}/download`

Download report file.

**Response (200):**
Binary file content

---

### Search Reports

**GET** `/reports/search`

Search medical reports.

**Query Parameters:**
- `query` (string, required): Search query
- `skip` (integer, default: 0): Number of records to skip
- `limit` (integer, default: 10): Number of records to return

**Response (200):**
Array of matching reports

---

## Error Responses

### 400 Bad Request
```json
{
  "detail": "Invalid request data"
}
```

### 401 Unauthorized
```json
{
  "detail": "Invalid or expired token"
}
```

### 403 Forbidden
```json
{
  "detail": "Access denied"
}
```

### 404 Not Found
```json
{
  "detail": "Resource not found"
}
```

### 500 Internal Server Error
```json
{
  "detail": "Internal server error",
  "error_type": "ServerError"
}
```

---

## Rate Limiting

API endpoints are rate-limited to 100 requests per hour per user.

Rate limit information is included in response headers:
- `X-RateLimit-Limit`: 100
- `X-RateLimit-Remaining`: 99
- `X-RateLimit-Reset`: 1704110400

---

## Webhooks (Future)

Webhook support for real-time notifications is planned for v2.0.
