from datetime import datetime
from pydantic import BaseModel, Field


class Endpoint(BaseModel):
    ip: str
    port: int | None = None


class NetworkEvent(BaseModel):
    event_id: str
    timestamp: datetime

    source: Endpoint
    destination: Endpoint

    protocol: str
    event_type: str

    source_tool: str

    metadata: dict = Field(default_factory=dict)
