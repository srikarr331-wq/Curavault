"""Medical Report model"""

from enum import Enum

from sqlalchemy import Enum as SQLEnum, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import BaseModel


class ReportType(str, Enum):
    """Report types"""
    BLOOD_TEST = "blood_test"
    MRI = "mri"
    CT_SCAN = "ct_scan"
    X_RAY = "x_ray"
    ULTRASOUND = "ultrasound"
    ECG = "ecg"
    THYROID = "thyroid"
    VACCINATION = "vaccination"
    GENERAL = "general"


class Report(BaseModel):
    """Medical Report model"""

    __tablename__ = "reports"

    user_id: Mapped[str] = mapped_column(
        String(36),
        ForeignKey("users.id"),
        index=True,
    )
    title: Mapped[str] = mapped_column(String(255))
    description: Mapped[str] = mapped_column(Text, nullable=True)
    report_type: Mapped[ReportType] = mapped_column(SQLEnum(ReportType))
    file_url: Mapped[str] = mapped_column(String(500))
    file_size: Mapped[int] = mapped_column()
    mime_type: Mapped[str] = mapped_column(String(50))
    test_date: Mapped[str] = mapped_column(String(50), nullable=True)
    doctor_name: Mapped[str] = mapped_column(String(255), nullable=True)
    lab_name: Mapped[str] = mapped_column(String(255), nullable=True)
    extracted_text: Mapped[str] = mapped_column(Text, nullable=True)
    ai_summary: Mapped[str] = mapped_column(Text, nullable=True)
