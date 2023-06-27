import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()

psql_user = os.getenv('POSTGRES_USER')
psql_password = os.getenv('POSTGRES_PASSWORD')
psql_server = os.getenv('POSTGRES_SERVER')
psql_port = os.getenv('POSTGRES_PORT')
psql_db = os.getenv('POSTGRES_DB')

SQLALCHEMY_DATABASE_URL = "postgresql://{0}:{1}@{2}:{3}/{4}".format(
    psql_user, psql_password, psql_server, psql_port, psql_db
)
engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
