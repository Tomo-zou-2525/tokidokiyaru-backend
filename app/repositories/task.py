
from sqlalchemy.orm import Session

from app.models.task import Task
from app.schemas import schemas


def get_tasks(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Task).offset(skip).limit(limit).all()


def create_task(db: Session, task: schemas.TaskCreate):
    db_task = Task(
        user_id=task.user_id,
        name=task.name,
        order=task.order
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task
