"""User Schemas"""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class UserBase(BaseModel):
    """Base User schema"""
    email: EmailStr
    full_name: str = Field(..., min_length=1, max_length=255)
    phone: Optional[str] = None


class UserCreate(UserBase):
    """User creation schema"""
    password: str = Field(..., min_length=8, max_length=255)
    confirm_password: str


class UserLogin(BaseModel):
    """User login schema"""
    email: EmailStr
    password: str


class UserResponse(UserBase):
    """User response schema"""
    id: str
    role: str
    is_active: bool
    is_verified: bool
    email_verified_at: Optional[datetime]
    last_login: Optional[datetime]
    created_at: datetime
    updated_at: datetime

    class Config:
        """Pydantic config"""
        from_attributes = True


class TokenResponse(BaseModel):
    """Token response schema"""
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
    expires_in: int
