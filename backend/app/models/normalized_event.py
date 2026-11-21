from datetime import datetime
from pydantic import BaseModel, Field


class NormalizedEvent(BaseModel):
    event_id: str
    timestamp: datetime

    source_ip: str | None = None
    source_port: int | None = None

    destination_ip: str | None = None
    destination_port: int | None = None

    protocol: str | None = None

    event_type: str
    source_tool: str

    severity: int = 0

    metadata: dict = Field(default_factory=dict)
