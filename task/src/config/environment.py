import os

DEBUG = os.getenv("DEBUG", 'false').lower() in ('true', '1', 't')

#DB CONFIG

PORT = os.environ.get('PORT')
DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_PORT = os.getenv('DB_PORT')
DB_USER = os.getenv('DB_USER')

AUTH_SERVER = os.getenv('AUTH_SERVER')