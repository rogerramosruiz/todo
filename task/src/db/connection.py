from contextlib import contextmanager
from config.environment import DB_HOST, DB_NAME, DB_USER, DB_PASSWORD, DB_PORT
import psycopg2


@contextmanager
def connection():
    """
    Connection to database
    """
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            port = DB_PORT,
            password=DB_PASSWORD)
        
        cursor = conn.cursor()
        yield cursor, conn
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()
