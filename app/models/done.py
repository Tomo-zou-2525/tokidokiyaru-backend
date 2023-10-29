from sqlalchemy import Column, Integer, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship

from app.db.base_class import Base
from app.models.base import ModelBase


class Done(Base, ModelBase):
    __tablename__ = "dones"
    task_id = Column(Integer, ForeignKey("tasks.id", ondelete="CASCADE"), nullable=False)
    done_at = Column(DateTime, nullable=False, server_default=func.now())
    task = relationship("Task", back_populates="dones")
