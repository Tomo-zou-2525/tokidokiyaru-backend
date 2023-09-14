
from sqlalchemy.orm import Session

from app.models.run_date import RunDate
from app.schemas.run_date import RunDateCreate


class RunDateRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_run_date(self, run_date: RunDateCreate):
        db_run_date = RunDate(
            task_id=run_date.task_id,
            date=run_date.date
        )
        self.db.add(db_run_date)
        self.db.commit()
        self.db.refresh(db_run_date)
        return db_run_date
