"""Application Configuration"""

from functools import lru_cache
from typing import Optional

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings from environment variables"""

    # Application
    app_name: str = "CuraVault"
    app_version: str = "1.0.0"
    debug: bool = False
    environment: str = "development"

    # Database
    database_url: str = "postgresql://user:password@localhost/curavault"
    database_echo: bool = False

    # Redis
    redis_url: str = "redis://localhost:6379/0"

    # Elasticsearch
    elasticsearch_url: str = "http://localhost:9200"

    # Security
    secret_key: str = "change-me-in-production"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    refresh_token_expire_days: int = 7

    # CORS
    cors_origins: list = [
        "http://localhost:3000",
        "http://localhost:8000",
    ]
    cors_allow_credentials: bool = True
    cors_allow_methods: list = ["*"]
    cors_allow_headers: list = ["*"]

    # AWS S3
    aws_access_key_id: Optional[str] = None
    aws_secret_access_key: Optional[str] = None
    aws_s3_bucket_name: str = "curavault-uploads"
    aws_region: str = "us-east-1"

    # Email
    mailersend_api_key: Optional[str] = None
    mailersend_from_email: str = "noreply@curavault.io"
    mailersend_from_name: str = "CuraVault"

    # OTP
    otp_expire_minutes: int = 10
    otp_length: int = 6

    # File Upload
    max_upload_size_mb: int = 50
    allowed_file_types: list = ["pdf", "jpg", "jpeg", "png"]
    upload_directory: str = "./uploads"

    # Rate Limiting
    rate_limit_requests: int = 100
    rate_limit_period: int = 3600

    # Encryption
    encryption_key: str = "change-me-in-production-32-chars"

    # JWT
    jwt_algorithm: str = "HS256"
    jwt_expiration_hours: int = 24

    # Logging
    log_level: str = "INFO"

    class Config:
        """Pydantic config"""
        env_file = ".env"
        case_sensitive = False


@lru_cache()
def get_settings() -> Settings:
    """Get application settings"""
    return Settings()
