from sqlalchemy.orm import Session

from . import models, schemas


# Read
def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def get_tasks(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Task).offset(skip).limit(limit).all()


def get_run_dates(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.RunDate).offset(skip).limit(limit).all()

# Create


def create_user(db: Session, user: schemas.User):
    db_user = models.User(
        name=user.name,
        email=user.email,
        hashed_password=user.password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def create_task(db: Session, task: schemas.Task):
    db_task = models.Task(
        user_id=task.user_id,
        name=task.name,
        order=task.order
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


def create_run_date(db: Session, run_date: schemas.RunDate):
    db_run_date = models.RunDate(
        task_id=run_date.task_id,
        date=run_date.date
    )
    db.add(db_run_date)
    db.commit()
    db.refresh(db_run_date)
    return db_run_date

# Update

# Delete
