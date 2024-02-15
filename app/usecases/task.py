from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.task import Task
from app.repositories.task import task
from app.schemas.task import (
    TaskCreate,
    TaskResponse,
    TaskUpdate,
)


router = APIRouter()


@router.get("/{task_id}", response_model=TaskResponse)
def get_task(task_id: int, db: Session = Depends(get_db)) -> Task:
    return task.get(id=task_id, db=db)


@router.get("", response_model=list[TaskResponse])
def get_user_task_list(user_id: int, db: Session = Depends(get_db)) -> list[Task]:
    return task.get_user_task_list(user_id=user_id, db=db)


@router.post("", response_model=TaskResponse)
def create_task(data_in: TaskCreate, db: Session = Depends(get_db)) -> Task:
    return task.create(db=db, obj_in=data_in)


@router.put("/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, data_in: TaskUpdate, db: Session = Depends(get_db)) -> Task:
    return task.update(db=db, id=task_id, obj_in=data_in)


@router.delete("/{task_id}")
def hard_delete_task(task_id: int, db: Session = Depends(get_db)) -> str:
    task.hard_delete(db=db, id=task_id)
    return "Task deleted"
