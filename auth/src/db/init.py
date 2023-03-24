from pathlib import Path

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT 

from config.environment import DB_HOST, DB_NAME, DB_PASSWORD, DB_PORT, DB_USER, DB_INIT_SCRIPT_PATH
from db.connection import connection

def create_database():
    try:
        con = psycopg2.connect(            
                host=DB_HOST,
                user=DB_USER,
                password=DB_PASSWORD,
                port = DB_PORT)

        con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT);

        cursor = con.cursor();
        cursor.execute("SELECT * FROM pg_database WHERE datname = %s", (DB_NAME,))
        dbs = cursor.fetchone()
        
        if dbs is None:
            sqlCreateDatabase = f"CREATE DATABASE {DB_NAME};" 
            cursor.execute(sqlCreateDatabase);
        
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        con.close()



def create_tables():
    try:
        with connection() as (cur, conn):
            with open(Path(DB_INIT_SCRIPT_PATH), 'r') as f:
                sql = f.read()
            cur.execute(sql)
            conn.commit()

    except Exception as e:
        print(e)

def intialize():
    create_database()
    create_tables()