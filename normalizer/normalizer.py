from backend.app.models import NetworkEvent, Alert
from backend.app.models.normalized_event import NormalizedEvent


def normalize_network_event(event: NetworkEvent) -> NormalizedEvent:
    return NormalizedEvent(
        event_id=event.event_id,
        timestamp=event.timestamp,

        source_ip=event.source.ip,
        source_port=event.source.port,

        destination_ip=event.destination.ip,
        destination_port=event.destination.port,

        protocol=event.protocol,

        event_type=event.event_type,
        source_tool=event.source_tool,

        severity=0,

        metadata=event.metadata,
    )


def normalize_alert(alert: Alert) -> NormalizedEvent:
    return NormalizedEvent(
        event_id=alert.alert_id,
        timestamp=alert.timestamp,

        source_ip=alert.source_ip,
        destination_ip=alert.destination_ip,

        protocol=alert.metadata.get("protocol"),

        event_type="alert",
        source_tool=alert.source_tool,

        severity=alert.severity,

        metadata={
            "signature": alert.signature,
            **alert.metadata,
        },
    )
