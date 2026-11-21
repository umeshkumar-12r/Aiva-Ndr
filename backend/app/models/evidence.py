from pydantic import BaseModel


class Evidence(BaseModel):
    evidence_id: str

    hypothesis_id: str

    type: str

    description: str

    source_events: list[str]

    strength: float
