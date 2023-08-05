from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.repositories.run_date import RunDateRepository
from app.schemas.run_date import RunDateCreate, RunDateResponse

router = APIRouter()


@router.get("/rundates", response_model=List[RunDateResponse])
def read_run_dates(
        skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    run_date_repository = RunDateRepository(db)
    run_dates = run_date_repository.get_run_dates(skip=skip, limit=limit)
    return run_dates


@router.post("/rundates", response_model=RunDateResponse)
def create_run_date(run_date: RunDateCreate,
                    db: Session = Depends(get_db)):
    run_date_repository = RunDateRepository(db)
    return run_date_repository.create_run_date(run_date)
