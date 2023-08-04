
from sqlalchemy.orm import Session

from app.models.run_date import RunDate
from app.schemas import schemas


class RunDateRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_run_dates(self, skip: int = 0, limit: int = 100):
        return self.db.query(RunDate).offset(skip).limit(limit).all()

    def create_run_date(self, run_date: schemas.RunDateCreate):
        db_run_date = RunDate(
            task_id=run_date.task_id,
            date=run_date.date
        )
        self.db.add(db_run_date)
        self.db.commit()
        self.db.refresh(db_run_date)
        return db_run_date
