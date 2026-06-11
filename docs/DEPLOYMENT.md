# Deployment Guide

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Development Deployment](#development-deployment)
3. [Production Deployment](#production-deployment)
4. [Environment Configuration](#environment-configuration)
5. [Database Setup](#database-setup)
6. [CI/CD Pipeline](#cicd-pipeline)
7. [Monitoring & Logging](#monitoring--logging)
8. [Backup & Recovery](#backup--recovery)
9. [Scaling](#scaling)
10. [Troubleshooting](#troubleshooting)

---

## Prerequisites

- Docker & Docker Compose
- AWS Account (for S3, RDS, EC2)
- PostgreSQL 15+
- Redis 7+
- Elasticsearch 8+
- Node.js 18+
- Python 3.11+
- Git

---

## Development Deployment

### Local Setup

```bash
# Clone repository
git clone https://github.com/srikarr331-wq/curavault.git
cd curavault

# Copy environment file
cp backend/.env.example backend/.env

# Start Docker services
docker-compose up -d

# Backend setup
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python -m alembic upgrade head
python main.py

# Frontend setup (new terminal)
cd frontend
npm install
npm run dev
```

### Access Points

- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- API Docs: http://localhost:8000/docs
- Database: localhost:5432
- Redis: localhost:6379
- Elasticsearch: http://localhost:9200

---

## Production Deployment

### Option 1: AWS EC2 + RDS + S3

#### Step 1: Launch EC2 Instance

```bash
# Launch Ubuntu 22.04 LTS instance
# t3.medium or larger recommended
# Security group: Allow ports 80, 443, 22

# SSH into instance
ssh -i key.pem ubuntu@<public-ip>

# Update system
sudo apt update && sudo apt upgrade -y

# Install Docker
sudo apt install -y docker.io docker-compose
sudo usermod -aG docker $USER

# Install Git
sudo apt install -y git
```

#### Step 2: Configure RDS Database

```bash
# Create RDS PostgreSQL 15 instance
# - Engine: PostgreSQL 15.3
# - Instance class: db.t3.small (minimum)
# - Storage: 100 GB, encrypted
# - Backup retention: 30 days
# - Multi-AZ: Enabled
# - VPC: Same as EC2

# Get endpoint from AWS Console
RDS_ENDPOINT="curavault-db.xxxx.rds.amazonaws.com"
```

#### Step 3: Create S3 Bucket

```bash
# Create S3 bucket for file uploads
aws s3 mb s3://curavault-uploads --region us-east-1

# Enable encryption
aws s3api put-bucket-encryption \
  --bucket curavault-uploads \
  --server-side-encryption-configuration '{
    "Rules": [{
      "ApplyServerSideEncryptionByDefault": {
        "SSEAlgorithm": "AES256"
      }
    }]
  }'

# Block public access
aws s3api put-public-access-block \
  --bucket curavault-uploads \
  --public-access-block-configuration \
  "BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=true,RestrictPublicBuckets=true"
```

#### Step 4: Deploy Application

```bash
# Clone repository
git clone https://github.com/srikarr331-wq/curavault.git
cd curavault

# Create production .env
cat > .env.production << EOF
DATABASE_URL=postgresql://curavault:${DB_PASSWORD}@${RDS_ENDPOINT}:5432/curavault
REDIS_URL=redis://localhost:6379/0
ELASTICSEARCH_URL=http://localhost:9200
SECRET_KEY=$(python -c 'import secrets; print(secrets.token_urlsafe(32))')
AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY}
AWS_SECRET_ACCESS_KEY=${AWS_SECRET_KEY}
AWS_S3_BUCKET_NAME=curavault-uploads
ENVIRONMENT=production
DEBUG=false
EOF

# Build Docker images
docker-compose -f docker-compose.prod.yml build

# Start services
docker-compose -f docker-compose.prod.yml up -d

# Run migrations
docker-compose -f docker-compose.prod.yml exec backend \
  alembic upgrade head

# Create superuser
docker-compose -f docker-compose.prod.yml exec backend \
  python -m app.cli create-admin
```

### Option 2: Heroku Deployment

```bash
# Create Heroku app
heroku create curavault

# Add buildpacks
heroku buildpacks:add heroku/python
heroku buildpacks:add heroku/nodejs

# Set environment variables
heroku config:set \
  SECRET_KEY=$(python -c 'import secrets; print(secrets.token_urlsafe(32))') \
  ENVIRONMENT=production \
  DEBUG=false

# Add PostgreSQL addon
heroku addons:create heroku-postgresql:standard-0

# Add Redis addon
heroku addons:create heroku-redis:premium-0

# Deploy
git push heroku main

# Run migrations
heroku run alembic upgrade head
```

### Option 3: Google Cloud Run

```bash
# Build Docker image
cloud builds submit --tag gcr.io/PROJECT_ID/curavault:latest

# Deploy to Cloud Run
cloud run deploy curavault \
  --image gcr.io/PROJECT_ID/curavault:latest \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated \
  --set-env-vars DATABASE_URL=${DATABASE_URL}
```

---

## Environment Configuration

### Production Variables

```bash
# Application
APP_NAME=CuraVault
ENVIRONMENT=production
DEBUG=false

# Security
SECRET_KEY=<generate-random-secret>
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
REFRESH_TOKEN_EXPIRE_DAYS=7

# Database
DATABASE_URL=postgresql://user:password@host:5432/curavault
DATABASE_ECHO=false

# Redis
REDIS_URL=redis://:password@host:6379/0

# Elasticsearch
ELASTICSEARCH_URL=https://user:pass@host:9200

# AWS
AWS_ACCESS_KEY_ID=<your-access-key>
AWS_SECRET_ACCESS_KEY=<your-secret-key>
AWS_S3_BUCKET_NAME=curavault-uploads
AWS_REGION=us-east-1

# Email
MAILERSEND_API_KEY=<your-api-key>

# CORS
CORS_ORIGINS=["https://app.curavault.io"]
```

---

## Database Setup

### Schema Initialization

```bash
# Create database
psql -h localhost -U postgres
CREATE DATABASE curavault;
CREATE USER curavault WITH PASSWORD 'secure_password';
GRANT ALL PRIVILEGES ON DATABASE curavault TO curavault;
```

### Run Migrations

```bash
cd backend
alembic upgrade head
```

### Backup Database

```bash
# Full backup
pg_dump -h localhost -U curavault curavault > backup.sql

# Restore from backup
psql -h localhost -U curavault curavault < backup.sql
```

---

## CI/CD Pipeline

### GitHub Actions Workflow

```yaml
name: CI/CD Pipeline

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main, develop]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - name: Install dependencies
        run: |
          cd backend
          pip install -r requirements.txt
      - name: Run tests
        run: |
          cd backend
          pytest --cov=app --cov-report=xml
      - name: Upload coverage
        uses: codecov/codecov-action@v3

  deploy:
    needs: test
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main' && github.event_name == 'push'
    steps:
      - uses: actions/checkout@v3
      - name: Deploy to production
        run: |
          # Add deployment steps
          echo "Deploying to production..."
```

---

## Monitoring & Logging

### CloudWatch Configuration

```python
import logging
from pythonjsonlogger import jsonlogger

logger = logging.getLogger()
logHandler = logging.StreamHandler()
formatter = jsonlogger.JsonFormatter()
logHandler.setFormatter(formatter)
logger.addHandler(logHandler)
```

### Metrics to Monitor

- **Performance**: Response time, throughput, error rate
- **Infrastructure**: CPU, memory, disk usage
- **Database**: Connection pool, query performance
- **Security**: Failed login attempts, suspicious access

### Alerting Rules

- Error rate > 5%
- Response time > 2 seconds
- CPU usage > 80%
- Database connections near limit

---

## Backup & Recovery

### Automated Backups

```bash
# Daily backup script
#!/bin/bash
DATE=$(date +%Y%m%d_%H%M%S)
pg_dump -h $DB_HOST -U $DB_USER $DB_NAME | \
  gzip > backup_$DATE.sql.gz
aws s3 cp backup_$DATE.sql.gz s3://curavault-backups/
rm backup_$DATE.sql.gz
```

### Point-in-Time Recovery

```bash
# Restore from specific backup
aws s3 cp s3://curavault-backups/backup_20240101_120000.sql.gz .
gunzip backup_20240101_120000.sql.gz
psql -h localhost -U curavault curavault < backup_20240101_120000.sql
```

---

## Scaling

### Horizontal Scaling

```yaml
# Load balancer configuration
# AWS Application Load Balancer
- Target group: Backend API
- Health check: /health
- Min instances: 2
- Max instances: 10
- Auto-scaling policy: CPU > 70%
```

### Database Scaling

```bash
# RDS read replicas for read-heavy workloads
aws rds create-db-instance-read-replica \
  --db-instance-identifier curavault-read-1 \
  --source-db-instance-identifier curavault-main
```

---

## Troubleshooting

### Common Issues

**Database connection refused**
```bash
# Check database status
psql -h localhost -U postgres -c "SELECT version();"

# Verify credentials
echo $DATABASE_URL
```

**High memory usage**
```bash
# Check process memory
ps aux | grep python

# Restart service
docker-compose restart backend
```

**S3 permission denied**
```bash
# Verify IAM policy
aws iam get-user-policy --user-name curavault --policy-name s3-access
```

---

## References

- [FastAPI Deployment](https://fastapi.tiangolo.com/deployment/)
- [Docker Best Practices](https://docs.docker.com/develop/dev-best-practices/)
- [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/)
