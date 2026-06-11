"""Audit Log model"""

from enum import Enum

from sqlalchemy import Enum as SQLEnum, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import BaseModel


class AuditAction(str, Enum):
    """Audit actions"""
    LOGIN = "login"
    LOGOUT = "logout"
    UPLOAD_REPORT = "upload_report"
    DELETE_REPORT = "delete_report"
    DOWNLOAD_REPORT = "download_report"
    SHARE_ACCESS = "share_access"
    REVOKE_ACCESS = "revoke_access"
    UPDATE_PROFILE = "update_profile"
    CREATE_PRESCRIPTION = "create_prescription"
    VIEW_RECORD = "view_record"


class AuditLog(BaseModel):
    """Audit Log model"""

    __tablename__ = "audit_logs"

    user_id: Mapped[str] = mapped_column(String(36), nullable=True, index=True)
    action: Mapped[AuditAction] = mapped_column(SQLEnum(AuditAction), index=True)
    resource_type: Mapped[str] = mapped_column(String(100), nullable=True)
    resource_id: Mapped[str] = mapped_column(String(36), nullable=True)
    ip_address: Mapped[str] = mapped_column(String(45))
    user_agent: Mapped[str] = mapped_column(String(500), nullable=True)
    details: Mapped[str] = mapped_column(Text, nullable=True)
