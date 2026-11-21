from fastapi import APIRouter
from psycopg.types.json import Jsonb
from backend.app.models import NetworkEvent
from database.connection import get_connection

router = APIRouter(prefix="/events", tags=["Events"])


@router.post("/")
def create_event(event: NetworkEvent):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO events (
            event_id,
            timestamp,
            source_ip,
            source_port,
            destination_ip,
            destination_port,
            protocol,
            event_type,
            source_tool,
            metadata
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (event_id) DO NOTHING
        """,
        (
            event.event_id,
            event.timestamp,
            event.source.ip,
            event.source.port,
            event.destination.ip,
            event.destination.port,
            event.protocol,
            event.event_type,
            event.source_tool,
            Jsonb(event.metadata),
        ),
    )

    conn.commit()

    cur.close()
    conn.close()

    return {
        "message": "Event created successfully",
        "event": event
    }


@router.get("/")
def get_events():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT
            event_id,
            timestamp,
            source_ip,
            source_port,
            destination_ip,
            destination_port,
            protocol,
            event_type,
            source_tool,
            metadata
        FROM events
        ORDER BY timestamp DESC
        """
    )

    rows = cur.fetchall()

    cur.close()
    conn.close()

    events = []

    for row in rows:
        events.append({
            "event_id": row[0],
            "timestamp": row[1],
            "source": {
                "ip": row[2],
                "port": row[3]
            },
            "destination": {
                "ip": row[4],
                "port": row[5]
            },
            "protocol": row[6],
            "event_type": row[7],
            "source_tool": row[8],
            "metadata": row[9]
        })

    return {
        "count": len(events),
        "events": events
    }
