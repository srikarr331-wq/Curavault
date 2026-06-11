"""Report Schemas"""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class ReportCreate(BaseModel):
    """Report creation schema"""
    title: str = Field(..., min_length=1, max_length=255)
    description: Optional[str] = None
    report_type: str
    test_date: Optional[str] = None
    doctor_name: Optional[str] = None
    lab_name: Optional[str] = None


class ReportUpdate(BaseModel):
    """Report update schema"""
    title: Optional[str] = None
    description: Optional[str] = None
    doctor_name: Optional[str] = None
    lab_name: Optional[str] = None


class ReportResponse(BaseModel):
    """Report response schema"""
    id: str
    user_id: str
    title: str
    description: Optional[str]
    report_type: str
    test_date: Optional[str]
    doctor_name: Optional[str]
    lab_name: Optional[str]
    file_url: str
    file_size: int
    mime_type: str
    extracted_text: Optional[str]
    ai_summary: Optional[str]
    created_at: datetime
    updated_at: datetime

    class Config:
        """Pydantic config"""
        from_attributes = True
