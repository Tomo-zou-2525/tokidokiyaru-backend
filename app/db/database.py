import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

load_dotenv()

psql_user = os.getenv('PGUSER')
psql_password = os.getenv('PGPASSWORD')
psql_server = os.getenv('PGHOST')
psql_port = os.getenv('PGPORT')
psql_db = os.getenv('PGDATABASE')

SQLALCHEMY_DATABASE_URL = "postgresql://{0}:{1}@{2}:{3}/{4}".format(
    psql_user, psql_password, psql_server, psql_port, psql_db
)
engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
