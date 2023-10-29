from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.done import Done
from app.repositories.done import done
from app.schemas.done import (
    DoneCreate,
    DoneResponse,
    DoneUpdate,
)


router = APIRouter()


@router.get("/{id}", response_model=DoneResponse)
def get_done(id: int, db: Session = Depends(get_db)) -> Done:
    done_data = done.get(id=id, db=db)

    return done_data


@router.get("", response_model=List[DoneResponse])
def get_done_list(db: Session = Depends(get_db)) -> List[Done]:
    done_data = done.get_list(db=db)

    return done_data


@router.post("", response_model=DoneResponse)
def create_done(data_in: DoneCreate, db: Session = Depends(get_db)) -> Done:
    return done.create(db=db, obj_in=data_in)


@router.post("/rand", response_model=DoneResponse)
def create_rand_done(db: Session = Depends(get_db)) -> Done:
    data_in = DoneCreate(task_id=1)

    return done.create(db=db, obj_in=data_in)


@router.put("/{id}", response_model=DoneResponse)
def update_done(
    id: int, data_in: DoneUpdate, db: Session = Depends(get_db)
) -> Done:
    return done.update(db=db, id=id, obj_in=data_in)


@router.delete("/{id}", response_model=DoneResponse)
def hard_delete_done(id: int, db: Session = Depends(get_db)) -> Done:
    return done.hard_delete(db=db, id=id)
