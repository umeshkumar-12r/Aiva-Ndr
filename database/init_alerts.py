from database.connection import get_connection


conn = get_connection()
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS alerts (
    alert_id VARCHAR(255) PRIMARY KEY,
    timestamp TIMESTAMPTZ NOT NULL,

    source_ip VARCHAR(45),
    destination_ip VARCHAR(45),

    signature TEXT,
    severity INTEGER,

    source_tool VARCHAR(50),

    metadata JSONB DEFAULT '{}'::jsonb
);
""")

conn.commit()

cur.close()
conn.close()

print("Alerts table created successfully")
