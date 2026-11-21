from fastapi import APIRouter
from backend.app.models import Anomaly

router = APIRouter(prefix="/anomalies", tags=["Anomalies"])

anomalies = []


@router.post("/")
def create_anomaly(anomaly: Anomaly):
    anomalies.append(anomaly)

    return {
        "message": "Anomaly created successfully",
        "anomaly": anomaly
    }


@router.get("/")
def get_anomalies():
    return {
        "count": len(anomalies),
        "anomalies": anomalies
    }
