from datetime import datetime
from pydantic import BaseModel


class Anomaly(BaseModel):
    anomaly_id: str
    timestamp: datetime

    host_ip: str

    anomaly_score: float

    reasons: list[str]

    model: str
