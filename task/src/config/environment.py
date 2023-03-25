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

AUTH_SERVER = os.getenv('AUTH_SERVER')