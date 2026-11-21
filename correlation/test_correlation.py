from backend.app.models.normalized_event import NormalizedEvent
from correlation.engine import correlate_events


events = [
    NormalizedEvent(
        event_id="zeek-001",
        timestamp="2026-11-22T10:00:00Z",
        source_ip="172.19.173.111",
        source_port=50000,
        destination_ip="8.8.8.8",
        destination_port=53,
        protocol="udp",
        event_type="connection",
        source_tool="zeek",
        metadata={}
    ),

    NormalizedEvent(
        event_id="suricata-001",
        timestamp="2026-11-22T10:00:02Z",
        source_ip="172.19.173.111",
        destination_ip="8.8.8.8",
        protocol="icmp",
        event_type="alert",
        source_tool="suricata",
        severity=2,
        metadata={
            "signature": "AIVA-NDR TEST ICMP ALERT"
        }
    ),

    NormalizedEvent(
        event_id="zeek-002",
        timestamp="2026-11-22T10:00:10Z",
        source_ip="172.19.173.111",
        source_port=50001,
        destination_ip="8.8.8.8",
        destination_port=53,
        protocol="udp",
        event_type="connection",
        source_tool="zeek",
        metadata={}
    ),

    # Different source IP
    NormalizedEvent(
        event_id="zeek-003",
        timestamp="2026-11-22T10:00:05Z",
        source_ip="192.168.1.50",
        source_port=40000,
        destination_ip="1.1.1.1",
        destination_port=53,
        protocol="udp",
        event_type="connection",
        source_tool="zeek",
        metadata={}
    ),
]


activities = correlate_events(events)


for activity in activities:
    print("\nACTIVITY")
    print(activity.model_dump_json(indent=2))
