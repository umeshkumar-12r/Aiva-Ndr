import time
import requests
from datetime import datetime, timezone


LOG_FILE = "../live/conn.log"
API_URL = "http://127.0.0.1:8000/events/"


def parse_event(line, fields):

    values = line.rstrip("\n").split("\t")

    record = dict(zip(fields, values))

    return {
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


def send_event(event):

    response = requests.post(
        API_URL,
        json=event,
        timeout=5
    )

    response.raise_for_status()


def follow_log():

    fields = None

    with open(LOG_FILE, "r") as file:

        while True:

            line = file.readline()

            if not line:

                time.sleep(1)
                continue

            line = line.rstrip("\n")

            if line.startswith("#fields"):

                fields = line.split("\t")[1:]

                print("Detected Zeek fields")

                continue

            if line.startswith("#"):
                continue

            if not fields:
                continue

            try:

                event = parse_event(line, fields)

                send_event(event)

                print(
                    f"[INGESTED] "
                    f"{event['event_id']} "
                    f"{event['source']['ip']} → "
                    f"{event['destination']['ip']}"
                )

            except Exception as e:

                print(f"[ERROR] {e}")


if __name__ == "__main__":

    print("Starting Zeek ingestion worker...")

    follow_log()
