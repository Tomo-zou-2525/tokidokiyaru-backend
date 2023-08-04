
from sqlalchemy.orm import Session

from app.models.run_date import RunDate
from app.schemas import schemas


def get_run_dates(db: Session, skip: int = 0, limit: int = 100):
    return db.query(RunDate).offset(skip).limit(limit).all()


def create_run_date(db: Session, run_date: schemas.RunDateCreate):
    db_run_date = RunDate(
        task_id=run_date.task_id,
        date=run_date.date
    )
    db.add(db_run_date)
    db.commit()
    db.refresh(db_run_date)
    return db_run_date
