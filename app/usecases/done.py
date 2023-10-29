from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.task import Task
from app.repositories.done import done
from app.repositories.task import task
from app.schemas.done import (
    DoneCreate,
)
from app.schemas.task import TaskResponse


router = APIRouter()


@router.post("", response_model=TaskResponse)
def create_done(data_in: DoneCreate, db: Session = Depends(get_db)) -> Task:
    done.create(db=db, obj_in=data_in)
    return task.get_with_dones(id=data_in.task_id, db=db)


@router.delete("/{done_id}", response_model=TaskResponse)
def hard_delete_done(task_id: int, done_id: int, db: Session = Depends(get_db)) -> Task:
    done.hard_delete(db=db, id=done_id)
    return task.get_with_dones(id=task_id, db=db)
