from datetime import datetime
from pydantic import BaseModel, Field


class Alert(BaseModel):
    alert_id: str
    timestamp: datetime
    source_ip: str
    destination_ip: str
    signature: str
    severity: int
    source_tool: str
    metadata: dict = Field(default_factory=dict)
