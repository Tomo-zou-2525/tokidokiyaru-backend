from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.task import Task
from app.repositories.done import done
from app.schemas.done import (
    DoneCreate,
)
from app.schemas.task import TaskResponse


router = APIRouter()


@router.post("", response_model=TaskResponse)
def create_done(data_in: DoneCreate, db: Session = Depends(get_db)) -> Task:
    return done.create(db=db, obj_in=data_in)


@router.delete("/{id}", response_model=TaskResponse)
def hard_delete_done(id: int, db: Session = Depends(get_db)) -> Task:
    return done.hard_delete(db=db, id=id)
