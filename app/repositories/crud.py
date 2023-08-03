import hashlib

from sqlalchemy.orm import Session

from app.models.run_date import RunDate
from app.models.task import Task
from app.models.user import User
from app.schemas import schemas

# Read


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()


def get_tasks(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Task).offset(skip).limit(limit).all()


def get_run_dates(db: Session, skip: int = 0, limit: int = 100):
    return db.query(RunDate).offset(skip).limit(limit).all()

# Create


def create_user(db: Session, user: schemas.UserCreate):
    db_user = User(
        name=user.name,
        email=user.email,
        password=hashlib.sha256(user.password.encode()).hexdigest()
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


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


def create_run_date(db: Session, run_date: schemas.RunDateCreate):
    db_run_date = RunDate(
        task_id=run_date.task_id,
        date=run_date.date
    )
    db.add(db_run_date)
    db.commit()
    db.refresh(db_run_date)
    return db_run_date

# Update

# Delete
