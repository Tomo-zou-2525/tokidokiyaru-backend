from typing import List

from faker import Faker
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


@router.get("/{id}", response_model=TaskResponse)
def get_task(id: int, db: Session = Depends(get_db)) -> Task:
    task_data = task.get(id=id, db=db)

    return task_data


@router.get("", response_model=List[TaskResponse])
def get_task_list(db: Session = Depends(get_db)) -> List[Task]:
    task_data = task.get_list(db=db)

    return task_data


@router.post("", response_model=TaskResponse)
def create_task(data_in: TaskCreate, db: Session = Depends(get_db)) -> Task:
    return task.create(db=db, obj_in=data_in)


@router.post("/rand", response_model=TaskResponse)
def create_rand_task(db: Session = Depends(get_db)) -> Task:
    fake = Faker("ja_JP")
    data_in = TaskCreate(
        user_id=1,
        name=fake.job() + "の勉強",
    )

    return task.create(db=db, obj_in=data_in)


@router.put("/{id}", response_model=TaskResponse)
def update_task(id: int, data_in: TaskUpdate, db: Session = Depends(get_db)) -> Task:
    return task.update(db=db, id=id, obj_in=data_in)


@router.delete("/{id}", response_model=TaskResponse)
def hard_delete_task(id: int, db: Session = Depends(get_db)) -> Task:
    return task.hard_delete(db=db, id=id)
