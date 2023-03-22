from db.connection import connection

table = 'task'

def select(id_user ,limit:int = 30, offset:int = 0):
    """
    Get all tasks
    """
    with connection() as (cur, _):
        cur.execute(f'SELECT * FROM {table} WHERE id_user = %s ORDER BY id LIMIT %s OFFSET %s', (id_user, limit, offset, ))
        description = cur.description
        data = cur.fetchall()
        return data, description
    
def add(name, id_user):
    """
    Creates a new task
    """
    with connection() as (cur, conn):
        cur.execute("INSERT INTO task(name, done, id_user) VALUES(%s, %s, %s) RETURNING id",  (name, False, id_user))
        id = cur.fetchone()[0]
        conn.commit()
        return id


def edit(id, name, done):
    """
    Update task
    """
    with connection() as (cur, conn):
        cur.execute("UPDATE task SET name=%s, done=%s WHERE id = %s RETURNING id",  (name, done, id))
        conn.commit()
        return id
        
def delete(id):
    with connection() as (cur, conn):
        cur.execute(f"DELETE FROM {table} WHERE id = %s",  (id,))
        conn.commit()
        return True