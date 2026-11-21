import psycopg

conn = psycopg.connect(
    "host=127.0.0.1 dbname=aiva_ndr user=aiva_user password=aiva_password"
)

cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS events (
    event_id VARCHAR(100) PRIMARY KEY,
    timestamp TIMESTAMPTZ NOT NULL,

    source_ip VARCHAR(45) NOT NULL,
    source_port INTEGER,

    destination_ip VARCHAR(45) NOT NULL,
    destination_port INTEGER,

    protocol VARCHAR(20) NOT NULL,
    event_type VARCHAR(100) NOT NULL,
    source_tool VARCHAR(50) NOT NULL,

    metadata JSONB DEFAULT '{}'::jsonb
);
""")

conn.commit()

cur.close()
conn.close()

print("Events table created successfully")
