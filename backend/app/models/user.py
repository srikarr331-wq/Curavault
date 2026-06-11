"""User model"""

from datetime import datetime
from enum import Enum

from sqlalchemy import Boolean, Column, DateTime, Enum as SQLEnum, String
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import BaseModel


class UserRole(str, Enum):
    """User roles"""
    PATIENT = "patient"
    DOCTOR = "doctor"
    HOSPITAL_ADMIN = "hospital_admin"
    SYSTEM_ADMIN = "system_admin"


class User(BaseModel):
    """User model"""

    __tablename__ = "users"

    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    full_name: Mapped[str] = mapped_column(String(255))
    password_hash: Mapped[str] = mapped_column(String(255))
    phone: Mapped[str] = mapped_column(String(20), nullable=True)
    role: Mapped[UserRole] = mapped_column(
        SQLEnum(UserRole),
        default=UserRole.PATIENT,
    )
    is_active: Mapped[bool] = mapped_column(Boolean, default=False)
    is_verified: Mapped[bool] = mapped_column(Boolean, default=False)
    email_verified_at: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    last_login: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    last_login_ip: Mapped[str] = mapped_column(String(45), nullable=True)
    mfa_enabled: Mapped[bool] = mapped_column(Boolean, default=False)
    mfa_secret: Mapped[str] = mapped_column(String(255), nullable=True)
