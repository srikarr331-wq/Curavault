# CuraVault - Universal Health Record Wallet

![CuraVault Logo](https://img.shields.io/badge/CuraVault-Healthcare%20Platform-blue?style=flat-square)
![Python](https://img.shields.io/badge/Python-3.11+-blue?style=flat-square)
![React](https://img.shields.io/badge/React-18+-blue?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

## 🏥 Vision

CuraVault is a **patient-owned digital healthcare wallet** that enables individuals to securely store, manage, access, and share their complete medical history from anywhere.

Eliminating fragmented healthcare records and creating a unified health identity for every patient.

---

## 🎯 Problem Statement

### Current Healthcare Challenges:
- **Fragmented Records**: Medical data scattered across hospitals, clinics, labs, pharmacies
- **Patient Burden**: Repeated tests, lost reports, manual paper prescriptions
- **Doctor Limitations**: Incomplete patient history leads to suboptimal decisions
- **System Inefficiency**: Isolated systems with no interoperability
- **Emergency Delays**: Critical information unavailable during emergencies

### CuraVault Solution:
✅ **Unified Medical Records** - All health data in one secure place
✅ **Smart Sharing** - QR-based access control with expiry
✅ **AI-Powered Insights** - OCR extraction & health trend analysis
✅ **Emergency Access** - Critical health info instantly available
✅ **Complete Control** - Patient owns their data

---

## 👥 User Roles

### 🧑‍🤝‍🧑 Patients
- Register & manage account
- Upload medical reports (PDFs, images, scans)
- View personalized health timeline
- Generate secure QR sharing links
- Manage emergency health profile
- Control data access permissions
- View audit logs

### 👨‍⚕️ Doctors
- Secure patient access (with authorization)
- View complete medical history
- Add consultation notes
- Upload prescriptions
- Access shared records via QR scan

### 🏥 Hospital Admins
- Verify doctor credentials
- Manage organization settings
- Monitor platform usage
- Access analytics & reports

### 🔐 System Admins
- Platform configuration
- User management
- Audit log monitoring
- Security event tracking

---

## ✨ Core Features

### 1. **Authentication & Security**
- Email-based registration & login
- OTP verification
- Forgot password recovery
- JWT with refresh tokens
- Session management
- Brute force protection
- Rate limiting

### 2. **Patient Profile Management**
- Complete health profile (DOB, gender, blood group, height, weight)
- Allergy tracking
- Chronic conditions management
- Emergency contact information
- Profile visibility settings

### 3. **Medical Record Management**
- **Upload**: PDF reports, images, scans, prescriptions
- **Types**: Blood tests, MRI, CT scans, X-rays, ultrasounds, ECG, thyroid reports, vaccination certificates
- **Features**:
  - Smart categorization
  - Metadata editing
  - Full-text search
  - Version history
  - Download & share

### 4. **Smart Health Timeline**
- Auto-generated chronological health history
- Filter by year, type, date range
- Search functionality
- Visual timeline representation

### 5. **QR-Based Secure Sharing**
- Generate unique QR codes for records
- Set access expiry: 15 min, 1 hour, 24 hours, 7 days
- Doctor scans to access
- Instant revocation capability
- Access logs for transparency

### 6. **Emergency Health Card**
- Quick access emergency profile
- Blood group & allergies display
- Active medications & conditions
- Emergency contacts
- Scannable emergency QR code

### 7. **Doctor Portal**
- Patient search & discovery
- Shared records access
- Prescription creation
- Consultation notes
- Medical history timeline

### 8. **Comprehensive Audit Logs**
- Track all user activities
- Login/logout events
- File uploads & downloads
- Record sharing & access
- IP address logging
- Timestamp tracking

### 9. **Notifications**
- Email notifications
- In-app notification center
- Types: Share alerts, access expiry, new prescriptions, security alerts

### 10. **AI-Powered Features** (v2.0+)
- **OCR Extraction**: Automatically extract test names, values, units, dates
- **Medical Summaries**: Convert technical reports to plain language
- **Health Insights**: Risk analysis for diabetes, thyroid, BP, cholesterol
- **Smart Search**: Natural language queries ("Show thyroid reports from 2025")

---

## 🛠️ Technology Stack

### **Frontend**
```
React.js 18+
TypeScript
Tailwind CSS 3
React Router v6
Axios (HTTP client)
React Query (Data fetching)
Zod (Validation)
Zustand (State management)
React Hot Toast (Notifications)
QR Code JS (QR generation)
```

### **Backend**
```
FastAPI 0.104+
Python 3.11+
SQLAlchemy (ORM)
Pydantic (Validation)
Python-Jose (JWT)
Passlib (Password hashing)
Python-Multipart (File uploads)
Pillow (Image processing)
pdfplumber (PDF reading)
Elasticsearch (Search)
Redis (Caching)
```

### **Database**
```
PostgreSQL 15+
Redis 7+
Elasticsearch 8+
```

### **Storage & Infrastructure**
```
AWS S3 (File storage)
Docker & Docker Compose
GitHub Actions (CI/CD)
```

### **Security**
```
AES-256 Encryption
TLS 1.3
RBAC (Role-Based Access Control)
JWT Authentication
CSRF Protection
Rate Limiting
SQL Injection Prevention
```

---

## 📁 Project Structure

```
curavault/
├── frontend/                   # React application
│   ├── src/
│   │   ├── components/        # Reusable components
│   │   ├── pages/             # Page components
│   │   ├── services/          # API client services
│   │   ├── store/             # Zustand state management
│   │   ├── hooks/             # Custom React hooks
│   │   ├── utils/             # Utility functions
│   │   ├── types/             # TypeScript types
│   │   ├── styles/            # Global styles
│   │   └── App.tsx            # Main app component
│   ├── public/                # Static assets
│   ├── package.json
│   ├── tsconfig.json
│   ├── tailwind.config.js
│   └── vite.config.ts
│
├── backend/                    # FastAPI application
│   ├── app/
│   │   ├── api/
│   │   │   ├── routes/        # API endpoints
│   │   │   └── dependencies.py
│   │   ├── models/            # SQLAlchemy models
│   │   ├── schemas/           # Pydantic schemas
│   │   ├── services/          # Business logic
│   │   ├── security/          # Auth & encryption
│   │   ├── storage/           # File storage handlers
│   │   ├── utils/             # Utilities
│   │   ├── config.py          # Configuration
│   │   └── main.py            # FastAPI app
│   ├── migrations/            # Database migrations
│   ├── tests/                 # Test suite
│   ├── requirements.txt
│   ├── .env.example
│   └── Dockerfile
│
├── docker-compose.yml         # Services orchestration
├── .github/
│   └── workflows/             # CI/CD pipelines
├── docs/                      # Documentation
│   ├── API.md                 # API documentation
│   ├── DATABASE.md            # Database schema
│   ├── SECURITY.md            # Security guide
│   └── DEPLOYMENT.md          # Deployment guide
├── .gitignore
├── LICENSE
└── CONTRIBUTING.md
```

---

## 🚀 Quick Start

### Prerequisites
- Node.js 18+
- Python 3.11+
- PostgreSQL 15+
- Redis 7+
- Docker & Docker Compose

### Development Setup

**1. Clone Repository**
```bash
git clone https://github.com/srikarr331-wq/curavault.git
cd curavault
```

**2. Backend Setup**
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
# Update .env with your configuration
python -m alembic upgrade head
python main.py
```

**3. Frontend Setup**
```bash
cd frontend
npm install
npm run dev
```

**4. Using Docker (Recommended)**
```bash
docker-compose up -d
# Backend: http://localhost:8000
# Frontend: http://localhost:3000
# API Docs: http://localhost:8000/docs
```

---

## 📚 Documentation

- **[API Documentation](./docs/API.md)** - Complete REST API reference
- **[Database Schema](./docs/DATABASE.md)** - Tables, relationships, indexes
- **[Security Guide](./docs/SECURITY.md)** - Implementation details
- **[Deployment Guide](./docs/DEPLOYMENT.md)** - Production setup
- **[User Manual](./USER_MANUAL.md)** - End-user guide
- **[Contributing Guide](./CONTRIBUTING.md)** - Development standards

---

## 🔐 Security Features

✅ **End-to-End Encryption** - AES-256 for sensitive data
✅ **TLS 1.3** - All communications encrypted
✅ **JWT Authentication** - Stateless, scalable auth
✅ **RBAC** - Role-based access control
✅ **Rate Limiting** - Brute force protection
✅ **Audit Logs** - Complete activity tracking
✅ **CSRF Protection** - Token-based protection
✅ **Input Validation** - Prevent injection attacks
✅ **Secure File Upload** - Virus scanning ready
✅ **Privacy by Design** - PHI never exposed

---

## 🧪 Testing

```bash
# Backend tests
cd backend
pytest --cov=app --cov-report=html

# Frontend tests
cd frontend
npm run test

# E2E tests
npm run test:e2e
```

**Target Coverage**: 80%+

---

## 📊 API Endpoints

### Authentication
```
POST   /api/v1/auth/register          - Register new user
POST   /api/v1/auth/login             - Login
POST   /api/v1/auth/logout            - Logout
POST   /api/v1/auth/refresh-token     - Refresh JWT
POST   /api/v1/auth/forgot-password   - Password reset request
POST   /api/v1/auth/verify-otp        - OTP verification
```

### Medical Records
```
POST   /api/v1/reports/upload         - Upload report
GET    /api/v1/reports                - List reports
GET    /api/v1/reports/{id}           - Get report details
PUT    /api/v1/reports/{id}           - Update report metadata
DELETE /api/v1/reports/{id}           - Delete report
POST   /api/v1/reports/{id}/download  - Download report
GET    /api/v1/reports/search         - Search reports
```

### Sharing & Access
```
POST   /api/v1/share/create-qr        - Generate QR share link
GET    /api/v1/share/verify           - Verify shared access
POST   /api/v1/share/revoke           - Revoke access
GET    /api/v1/share/history          - View share history
```

### Patient Profile
```
GET    /api/v1/profile                - Get patient profile
PUT    /api/v1/profile                - Update profile
POST   /api/v1/profile/emergency      - Update emergency card
GET    /api/v1/profile/timeline       - Get health timeline
```

### Doctor Portal
```
GET    /api/v1/doctor/patients        - Search patients
POST   /api/v1/doctor/consultation    - Add consultation note
GET    /api/v1/doctor/patient/{id}    - Get patient details
POST   /api/v1/doctor/prescription    - Create prescription
```

---

## 🎨 UI/UX Design

**Theme**: Healthcare Professional Design
**Color Palette**: Blue (#0066CC) / White (#FFFFFF) / Gray (#F5F5F5)
**Typography**: Clean, readable, accessible
**Layout**: Responsive, mobile-first design
**Accessibility**: WCAG 2.1 AA compliant

---

## 📈 Roadmap

### Phase 1 (v1.0) - MVP
- ✅ Authentication & authorization
- ✅ Basic record management
- ✅ QR-based sharing
- ✅ Emergency card
- ✅ Audit logs

### Phase 2 (v1.5) - Enhanced Features
- 🔄 AI OCR extraction
- 🔄 Medical summaries
- 🔄 Health insights
- 🔄 Smart search

### Phase 3 (v2.0) - Enterprise
- 🔄 FHIR compliance
- 🔄 Integration marketplace
- 🔄 Advanced analytics
- 🔄 Insurance integration

---

## 🤝 Contributing

We welcome contributions! Please read [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines.

### Development Workflow
1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

---

## 📝 License

This project is licensed under the MIT License - see [LICENSE](./LICENSE) file for details.

---

## 📞 Support & Contact

- **Issues**: [GitHub Issues](https://github.com/srikarr331-wq/curavault/issues)
- **Email**: support@curavault.io
- **Documentation**: [docs/](./docs/)

---

## 🙏 Acknowledgments

Built with ❤️ for better healthcare data management.

---

**CuraVault** - *Patient-Owned Health Records*