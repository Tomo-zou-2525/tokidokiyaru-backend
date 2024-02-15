from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base
from app.models.base import ModelBase


class Task(Base, ModelBase):
    __tablename__ = "tasks"
    name = Column(String(255), nullable=False, server_default="")
    dones = relationship("Done", back_populates="task", cascade="all")
