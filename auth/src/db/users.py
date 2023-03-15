from db.connection import connection

table = 'users'

def insert(username, hashed_password):
    with connection() as (cur, conn):
        cur.execute(f'INSERT INTO {table}(username, hashed_password) values(%s, %s) RETURNING id',  (username, hashed_password,))
        id = cur.fetchone()[0] 
        conn.commit()
        return id
    

def select_one_by(parm: str, value):
    with connection() as (cur, _):
        cur.execute(f'SELECT * FROM {table} WHERE {parm} = %s',  (value,))
        return cur.fetchone()