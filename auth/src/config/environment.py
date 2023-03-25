import os

DEBUG = os.getenv("DEBUG", 'false').lower() in ('true', '1', 't')

#DB CONFIG

PORT = os.environ.get('PORT')
DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('POSTGRES_USER')
DB_PASSWORD = os.getenv('POSTGRES_PASSWORD')
DB_PORT = os.getenv('DB_PORT')
DB_INIT_SCRIPT_PATH = os.getenv('DB_INIT_SCRIPT_PATH')

# JWT SECRETS

ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')
REFRESH_TOKEN_SECRET = os.getenv('REFRESH_TOKEN_SECRET')

ACCESS_TIME = {
    'days': int(os.environ.get('ACCESS_DAYS')),
    'hours': int(os.environ.get('ACCESS_HOURS')),
    'minutes': int(os.environ.get('ACCESS_MINUTES')),
    'seconds' : int(os.environ.get('ACCESS_SECONDS'))
}
    
REFRESH_TIME = {
    'days': int(os.environ.get('REFRESH_DAYS')),
    'hours': int(os.environ.get('REFRESH_HOURS')),
    'minutes': int(os.environ.get('REFRESH_MINUTES')),
    'seconds' : int(os.environ.get('REFRESH_SECONDS'))
}

#REDIS

REDIS_HOST = os.environ.get('REDIS_HOST')
REDIS_PORT = os.environ.get('REDIS_PORT')
REDIS_PASSWORD = os.environ.get('REDIS_PASSWORD')