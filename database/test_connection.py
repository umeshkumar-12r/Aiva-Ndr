import psycopg

conn = psycopg.connect(
    "host=127.0.0.1 dbname=aiva_ndr user=aiva_user password=aiva_password"
)

print("PostgreSQL connection successful")

conn.close()

