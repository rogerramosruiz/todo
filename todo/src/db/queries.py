from db.connection import connection

def select(table: str, limit = 10, offset = 0):
    with connection() as (cur, _):
        cur.execute(f'SELECT * FROM {table} ORDER BY id LIMIT %s OFFSET %s', (limit, offset, ))
        description = cur.description
        data = cur.fetchall()
        return data, description
            
def select_one(table, id):
    with connection() as (cur, _):
        cur.execute(f'SELECT * FROM {table} WHERE id = %s', (id, ))
        description = cur.description
        data = cur.fetchone()
        return data, description

def delete(table, id):
    with connection() as (cur, conn):
        cur.execute(f"DELETE FROM {table} WHERE id = %s",  (id,))
        conn.commit()
        return True