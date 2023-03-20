from redis import Redis
from redis.exceptions import ConnectionError
from config.environment import REDIS_HOST, REDIS_PASSWORD, REDIS_PORT

redis_client = None
try:
    redis_client = Redis(
        host = REDIS_HOST,
        port = REDIS_PORT, 
        password = REDIS_PASSWORD
    )
except ConnectionError as e:
    print(e)


