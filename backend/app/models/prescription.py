"""Prescription model"""

from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import BaseModel


class Prescription(BaseModel):
    """Prescription model"""

    __tablename__ = "prescriptions"

    user_id: Mapped[str] = mapped_column(
        String(36),
        ForeignKey("users.id"),
        index=True,
    )
    doctor_id: Mapped[str] = mapped_column(
        String(36),
        ForeignKey("doctors.id"),
        nullable=True,
    )
    medicine_name: Mapped[str] = mapped_column(String(255))
    dosage: Mapped[str] = mapped_column(String(100))
    frequency: Mapped[str] = mapped_column(String(100))
    duration: Mapped[str] = mapped_column(String(100))
    notes: Mapped[str] = mapped_column(Text, nullable=True)
    file_url: Mapped[str] = mapped_column(String(500), nullable=True)
    is_active: Mapped[bool] = mapped_column(default=True)
