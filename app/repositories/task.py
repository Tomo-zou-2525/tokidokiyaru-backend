
from sqlalchemy.orm import Session

from app.models.task import Task
from app.schemas import schemas


class TaskRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_tasks(self, skip: int = 0, limit: int = 100):
        return self.db.query(Task).offset(skip).limit(limit).all()

    def create_task(self, task: schemas.TaskCreate):
        db_task = Task(
            user_id=task.user_id,
            name=task.name,
            order=task.order
        )
        self.db.add(db_task)
        self.db.commit()
        self.db.refresh(db_task)
        return db_task
