from redis_client.connection import redis_client

def add(key, value, expiration = None):
    try:
        return redis_client.set(key, value, ex = expiration)
    except Exception as e:
        print(e)

def exists(key):
    try:
        return redis_client.exists(key) == 1
    except Exception as e:
        print(e)