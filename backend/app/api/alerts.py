from fastapi import APIRouter
from psycopg.types.json import Jsonb

from backend.app.models import Alert
from database.connection import get_connection

router = APIRouter(prefix="/alerts", tags=["Alerts"])


@router.post("/")
def create_alert(alert: Alert):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO alerts (
            alert_id,
            timestamp,
            source_ip,
            destination_ip,
            signature,
            severity,
            source_tool,
            metadata
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (alert_id) DO NOTHING
        """,
        (
            alert.alert_id,
            alert.timestamp,
            alert.source_ip,
            alert.destination_ip,
            alert.signature,
            alert.severity,
            alert.source_tool,
            Jsonb(alert.metadata),
        ),
    )

    conn.commit()

    cur.close()
    conn.close()

    return {
        "message": "Alert created successfully",
        "alert": alert
    }


@router.get("/")
def get_alerts():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT
            alert_id,
            timestamp,
            source_ip,
            destination_ip,
            signature,
            severity,
            source_tool,
            metadata
        FROM alerts
        ORDER BY timestamp DESC
        """
    )

    rows = cur.fetchall()

    cur.close()
    conn.close()

    alerts = []

    for row in rows:
        alerts.append({
            "alert_id": row[0],
            "timestamp": row[1],
            "source_ip": row[2],
            "destination_ip": row[3],
            "signature": row[4],
            "severity": row[5],
            "source_tool": row[6],
            "metadata": row[7],
        })

    return {
        "count": len(alerts),
        "alerts": alerts
    }
