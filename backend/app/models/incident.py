from datetime import datetime
from pydantic import BaseModel


class Incident(BaseModel):
    incident_id: str

    title: str

    status: str

    risk: str

    confidence: float

    hypotheses: list[str]

    mitre_techniques: list[str]

    created_at: datetime

    reason: str
