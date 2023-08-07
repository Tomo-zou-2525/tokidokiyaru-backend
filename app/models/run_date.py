from sqlalchemy import Column, DateTime, ForeignKey, Integer

from app.db.base import Base


class RunDate(Base):
    __tablename__ = "rundates"
    id = Column(Integer, primary_key=True, index=True)
    task_id = Column(Integer, ForeignKey("tasks.id"), index=True)
    date = Column(DateTime)
