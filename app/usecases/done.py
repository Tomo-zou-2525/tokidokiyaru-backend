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
    return task.get(id=data_in.task_id, db=db)


@router.delete("/{done_id}")
def hard_delete_done(done_id: int, db: Session = Depends(get_db)) -> str:
    done.hard_delete(db=db, id=done_id)
    return "Done deleted"
