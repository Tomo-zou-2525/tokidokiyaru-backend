from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.run_date import RunDate
from app.repositories.run_date import run_date
from app.schemas.run_date import (
    RunDateCreate,
    RunDateResponse,
    RunDateUpdate,
)


router = APIRouter()


@router.get("/{id}", response_model=RunDateResponse)
def get_run_date(id: int, db: Session = Depends(get_db)) -> RunDate:
    run_date_data = run_date.get(id=id, db=db)

    return run_date_data


@router.get("", response_model=List[RunDateResponse])
def get_run_date_list(db: Session = Depends(get_db)) -> List[RunDate]:
    run_date_data = run_date.get_list(db=db)

    return run_date_data


@router.post("", response_model=RunDateResponse)
def create_run_date(data_in: RunDateCreate, db: Session = Depends(get_db)) -> RunDate:
    return run_date.create(db=db, obj_in=data_in)


@router.post("/rand", response_model=RunDateResponse)
def create_rand_run_date(db: Session = Depends(get_db)) -> RunDate:
    data_in = RunDateCreate(task_id=1)

    return run_date.create(db=db, obj_in=data_in)


@router.put("/{id}", response_model=RunDateResponse)
def update_run_date(
    id: int, data_in: RunDateUpdate, db: Session = Depends(get_db)
) -> RunDate:
    return run_date.update(db=db, id=id, obj_in=data_in)


@router.delete("/{id}", response_model=RunDateResponse)
def hard_delete_run_date(id: int, db: Session = Depends(get_db)) -> RunDate:
    return run_date.hard_delete(db=db, id=id)
