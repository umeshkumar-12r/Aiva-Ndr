from pydantic import BaseModel


class Hypothesis(BaseModel):
    hypothesis_id: str
    title: str
    status: str

    confidence: float

    source_ip: str | None = None

    related_events: list[str]

    reason: str
