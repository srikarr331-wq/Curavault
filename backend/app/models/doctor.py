"""Doctor model"""

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import BaseModel


class Doctor(BaseModel):
    """Doctor model"""

    __tablename__ = "doctors"

    user_id: Mapped[str] = mapped_column(
        String(36),
        ForeignKey("users.id"),
        unique=True,
    )
    license_number: Mapped[str] = mapped_column(String(50), unique=True)
    specialization: Mapped[str] = mapped_column(String(255), nullable=True)
    hospital_id: Mapped[str] = mapped_column(
        String(36),
        ForeignKey("hospitals.id"),
        nullable=True,
    )
    bio: Mapped[str] = mapped_column(String(1000), nullable=True)
    profile_image_url: Mapped[str] = mapped_column(String(500), nullable=True)
