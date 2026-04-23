from pydantic import Field
from typing import Optional, List
from datetime import datetime
from beanie import Document, Link
from app.models.user import User

class Prediction(Document):
    user: Link[User]
    job_description: str
    job_title: Optional[str] = ""
    requirements: Optional[str] = ""
    prediction_result: str # "Real" or "Fake"
    confidence_score: float
    confidence_level: Optional[str] = "LOW"
    explanation: Optional[List[str]] = []
    created_at: datetime = Field(default_factory=datetime.utcnow)

    class Settings:
        name = "predictions"
