import requests
from datetime import datetime, timezone


API_URL = "http://127.0.0.1:8000/events/"


def parse_conn_log(filepath):

    events = []

    fields = None

    with open(filepath, "r") as file:

        for line in file:

            line = line.rstrip("\n")

            if line.startswith("#fields"):
                fields = line.split("\t")[1:]
                continue

            if line.startswith("#"):
                continue

            if not fields:
                continue

            values = line.split("\t")

            record = dict(zip(fields, values))

            event = {
                "event_id": record["uid"],

                "timestamp": datetime.fromtimestamp(
                    float(record["ts"]),
                    timezone.utc
                ).isoformat(),

                "source": {
                    "ip": record["id.orig_h"],
                    "port": int(record["id.orig_p"])
                },

                "destination": {
                    "ip": record["id.resp_h"],
                    "port": int(record["id.resp_p"])
                },

                "protocol": record["proto"],

                "event_type": "connection",

                "source_tool": "zeek",

                "metadata": {
                    "service": record["service"],
                    "duration": record["duration"],
                    "orig_bytes": record["orig_bytes"],
                    "resp_bytes": record["resp_bytes"],
                    "conn_state": record["conn_state"],
                    "history": record["history"],
                    "orig_pkts": record["orig_pkts"],
                    "resp_pkts": record["resp_pkts"],
                    "missed_bytes": record["missed_bytes"]
                }
            }

            events.append(event)

    return events


def send_event(event):

    response = requests.post(
        API_URL,
        json=event,
        timeout=5
    )

    response.raise_for_status()

    return response.json()


if __name__ == "__main__":

    filepath = "../test/conn.log"

    events = parse_conn_log(filepath)

    print(f"Parsed events: {len(events)}")

    for event in events:

        try:

            result = send_event(event)

            print(
                f"[SENT] {event['event_id']} "
                f"{event['source']['ip']} → "
                f"{event['destination']['ip']}"
            )

        except requests.RequestException as e:

            print(
                f"[ERROR] Could not send "
                f"{event['event_id']}: {e}"
            )
