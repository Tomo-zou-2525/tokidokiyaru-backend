from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.repositories.task import TaskRepository
from app.schemas.task import TaskCreate, TaskResponse

router = APIRouter()


@router.get("/tasks", response_model=List[TaskResponse])
def read_tasks(
        skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    task_repository = TaskRepository(db)
    tasks = task_repository.get_tasks(skip=skip, limit=limit)
    return tasks


@router.post("/tasks", response_model=TaskResponse)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    task_repository = TaskRepository(db)
    return task_repository.create_task(task)
