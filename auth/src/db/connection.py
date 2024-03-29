from contextlib import contextmanager
from config.environment import DB_HOST, DB_NAME, DB_USER, DB_PASSWORD, DB_PORT
import psycopg2


@contextmanager
def connection():
    """
    Connects to the data base
    """
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD)
        cursor = conn.cursor()
        yield cursor, conn
    finally:
        cursor.close()
        conn.close()
