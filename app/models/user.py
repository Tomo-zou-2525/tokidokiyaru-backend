from sqlalchemy import Column, Integer, String

from app.db.base_class import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True, nullable=True, index=True)
    password = Column(String, nullable=True)
