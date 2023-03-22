from .connection import connection
from db import queries

table = 'task'

def select_task(limit, offset):
    """
    Get all tasks
    """
    return queries.select(table, limit, offset)
    

def select_one(id):
    """
    Select one task
    """
    return queries.select_one(table, id)
    
def add(name):
    """
    Creates a new task
    """
    with connection() as (cur, conn):
        cur.execute("INSERT INTO task(name, done) VALUES(%s, %s) RETURNING id",  (name, False))
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
   queries.delete(table, id)