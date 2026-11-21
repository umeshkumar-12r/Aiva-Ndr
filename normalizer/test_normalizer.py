from backend.app.models import NetworkEvent, Alert
from normalizer.normalizer import (
    normalize_network_event,
    normalize_alert,
)


zeek_event = NetworkEvent(
    event_id="zeek-test-001",
    timestamp="2026-11-22T10:00:00Z",

    source={
        "ip": "172.19.173.111",
        "port": 54321
    },

    destination={
        "ip": "8.8.8.8",
        "port": 53
    },

    protocol="udp",
    event_type="connection",
    source_tool="zeek",

    metadata={
        "service": "dns",
        "orig_bytes": "100",
        "resp_bytes": "200"
    }
)


suricata_alert = Alert(
    alert_id="suricata-test-001",
    timestamp="2026-11-22T10:00:02Z",

    source_ip="172.19.173.111",
    destination_ip="8.8.8.8",

    signature="Test DNS Alert",
    severity=2,

    source_tool="suricata",

    metadata={
        "protocol": "UDP",
        "signature_id": 1000002,
        "category": "Test"
    }
)


normalized_zeek = normalize_network_event(zeek_event)
normalized_suricata = normalize_alert(suricata_alert)


print("ZEek:")
print(normalized_zeek.model_dump_json(indent=2))

print("\nSuricata:")
print(normalized_suricata.model_dump_json(indent=2))
