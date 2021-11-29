import os

PG_HOST = os.getenv('PG_HOST')
PG_PORT = os.getenv('PG_PORT')
PG_USER = os.getenv('PG_USER')
PG_PASSWORD = os.getenv('PG_PASSWORD')
PG_DBNAME = os.getenv('PG_DBNAME')

POSTGRES_DB_URL = f'postgresql://{PG_USER}:{PG_PASSWORD}@db:{PG_PORT}/{PG_DBNAME}'

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = POSTGRES_DB_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False
