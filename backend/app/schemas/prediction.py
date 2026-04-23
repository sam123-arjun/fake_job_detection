from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

class PredictionBase(BaseModel):
    job_description: str
    job_title: Optional[str] = ""
    requirements: Optional[str] = ""

class PredictionCreate(PredictionBase):
    pass

class PredictionResponse(BaseModel):
    id: Optional[str] = None
    job_description: Optional[str] = None
    job_title: Optional[str] = None
    requirements: Optional[str] = None
    prediction_result: Optional[str] = None
    confidence_score: Optional[float] = None
    confidence_level: Optional[str] = None # LOW, MEDIUM, HIGH
    explanation: Optional[List[str]] = None
    created_at: Optional[datetime] = None

    class Config:
        from_attributes = True
        populate_by_name = True
