from sqlalchemy import Column, ForeignKey, Integer, String

from app.db.database import Base


class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), index=True)
    name = Column(String)
    order = Column(Integer, unique=True)
