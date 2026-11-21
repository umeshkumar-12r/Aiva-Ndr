from datetime import datetime
from pydantic import BaseModel


class CorrelatedActivity(BaseModel):
    activity_id: str

    source_ip: str | None = None

    start_time: datetime
    end_time: datetime

    event_ids: list[str]

    event_count: int

    event_types: list[str]

    source_tools: list[str]
