from fastapi import FastAPI

from backend.app.api.events import router as events_router
from backend.app.api.alerts import router as alerts_router
from backend.app.api.anomalies import router as anomalies_router


app = FastAPI(
    title="AIVA-NDR",
    description="AI-powered Network Detection and Response System",
    version="0.1.0"
)


app.include_router(events_router)
app.include_router(alerts_router)
app.include_router(anomalies_router)


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "AIVA-NDR"
    }
