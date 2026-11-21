import json
import requests


API_URL = "http://127.0.0.1:8000/alerts/"
LOG_FILE = "/var/log/suricata/eve.json"


def parse_eve_line(line):
    data = json.loads(line)

    if data.get("event_type") != "alert":
        return None

    alert = data.get("alert", {})

    return {
        "alert_id": (
            f"suricata-"
            f"{data.get('flow_id')}-"
            f"{alert.get('signature_id')}-"
            f"{data.get('timestamp')}"
        ),
        "timestamp": data["timestamp"],
        "source_ip": data.get("src_ip"),
        "destination_ip": data.get("dest_ip"),
        "signature": alert.get("signature"),
        "severity": alert.get("severity"),
        "source_tool": "suricata",
        "metadata": {
            "action": alert.get("action"),
            "gid": alert.get("gid"),
            "signature_id": alert.get("signature_id"),
            "rev": alert.get("rev"),
            "category": alert.get("category"),
            "protocol": data.get("proto"),
            "source_port": data.get("src_port"),
            "destination_port": data.get("dest_port"),
            "alert_metadata": alert.get("metadata", {})
        }
    }


def send_alert(alert):
    response = requests.post(
        API_URL,
        json=alert,
        timeout=5
    )

    response.raise_for_status()

    return response.json()


if __name__ == "__main__":

    print("Reading Suricata alerts...")

    with open(LOG_FILE, "r") as file:

        for line in file:

            try:

                alert = parse_eve_line(line)

                if alert is None:
                    continue

                send_alert(alert)

                print(
                    f"[SENT] "
                    f"{alert['alert_id']} | "
                    f"{alert['source_ip']} → "
                    f"{alert['destination_ip']} | "
                    f"{alert['signature']}"
                )

            except Exception as e:

                print(f"[ERROR] {e}")
