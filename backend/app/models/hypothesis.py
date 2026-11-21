from pydantic import BaseModel


class Hypothesis(BaseModel):
    hypothesis_id: str

    title: str

    status: str

    confidence: float

    related_events: list[str]
