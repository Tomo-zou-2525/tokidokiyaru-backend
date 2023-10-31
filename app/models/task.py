from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base
from app.models.base import ModelBase


class Task(Base, ModelBase):
    __tablename__ = "tasks"
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    name = Column(String(255), nullable=False, server_default="")
    user = relationship("User", back_populates="tasks")
    dones = relationship("Done", back_populates="task", cascade="all")
