from sqlalchemy import Column, DateTime, ForeignKey, Integer
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class RunDate(Base):
    __tablename__ = "rundates"
    id = Column(Integer, primary_key=True, index=True)
    task_id = Column(Integer, ForeignKey("tasks.id"), index=True)
    date = Column(DateTime)
    task = relationship("Task", back_populates="rundates")
