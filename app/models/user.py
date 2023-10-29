from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base
from app.models.base import ModelBase


class User(Base, ModelBase):
    __tablename__ = "users"
    name = Column(String(255), nullable=False, server_default="")
    email = Column(String(255), unique=True, nullable=True)
    password = Column(String, nullable=True)
    tasks = relationship("Task", back_populates="user", cascade="all")
