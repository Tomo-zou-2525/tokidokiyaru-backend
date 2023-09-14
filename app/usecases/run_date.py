from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.repositories.run_date import RunDateRepository
from app.schemas.run_date import RunDateCreate, RunDateResponse

router = APIRouter()


@router.post("/rundates", response_model=RunDateResponse)
def create_run_date(run_date: RunDateCreate,
                    db: Session = Depends(get_db)):
    run_date_repository = RunDateRepository(db)
    return run_date_repository.create_run_date(run_date)
