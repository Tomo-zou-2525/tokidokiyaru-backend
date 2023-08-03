from sqlalchemy import Column, DateTime, ForeignKey, Integer

from ..db.database import Base


class RunDate(Base):
    __tablename__ = "rundates"
    id = Column(Integer, primary_key=True, index=True)
    task_id = Column(Integer, ForeignKey("tasks.id"), index=True)
    date = Column(DateTime, index=True)
