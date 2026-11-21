import psycopg


def get_connection():
    return psycopg.connect(
        "host=127.0.0.1 "
        "dbname=aiva_ndr "
        "user=aiva_user "
        "password=aiva_password"
    )
