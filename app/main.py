from typing import List

from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.repositories.run_date import RunDateRepository
from app.repositories.task import TaskRepository
from app.repositories.user import UserRepository
from app.schemas.run_date import RunDateCreate, RunDateResponse
from app.schemas.task import TaskCreate, TaskResponse
from app.schemas.user import UserCreate, UserResponse

app = FastAPI()


@app.get("/sample")
def sample():
    return {"message": "Hello World"}


# Read

@app.get("/users", response_model=List[UserResponse])
def read_users(
        skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    repository = UserRepository(db)
    users = repository.get_users(skip=skip, limit=limit)
    return users


@app.get("/tasks", response_model=List[TaskResponse])
def read_tasks(
        skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    task_repository = TaskRepository(db)
    tasks = task_repository.get_tasks(skip=skip, limit=limit)
    return tasks


@app.get("/rundates", response_model=List[RunDateResponse])
def read_run_dates(
        skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    run_date_repository = RunDateRepository(db)
    run_dates = run_date_repository.get_run_dates(skip=skip, limit=limit)
    return run_dates

# Create


@app.post("/users", response_model=UserResponse)
def create_user(
        user: UserCreate, db: Session = Depends(get_db)):
    repository = UserRepository(db)

    return repository.create_user(user=user)


@app.post("/tasks", response_model=TaskResponse)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    task_repository = TaskRepository(db)
    return task_repository.create_task(task)


@app.post("/rundates", response_model=RunDateResponse)
def create_run_date(run_date: RunDateCreate,
                    db: Session = Depends(get_db)):
    run_date_repository = RunDateRepository(db)
    return run_date_repository.create_run_date(run_date)
