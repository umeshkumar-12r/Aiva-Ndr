from pydantic import BaseModel


class MitreTechnique(BaseModel):
    technique_id: str
    name: str
    description: str
    confidence: float
