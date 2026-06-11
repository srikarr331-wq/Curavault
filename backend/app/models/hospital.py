"""Hospital model"""

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import BaseModel


class Hospital(BaseModel):
    """Hospital model"""

    __tablename__ = "hospitals"

    name: Mapped[str] = mapped_column(String(255), unique=True)
    address: Mapped[str] = mapped_column(String(500))
    city: Mapped[str] = mapped_column(String(100))
    state: Mapped[str] = mapped_column(String(100))
    pincode: Mapped[str] = mapped_column(String(10))
    phone: Mapped[str] = mapped_column(String(20))
    email: Mapped[str] = mapped_column(String(255))
    website: Mapped[str] = mapped_column(String(255), nullable=True)
    logo_url: Mapped[str] = mapped_column(String(500), nullable=True)
