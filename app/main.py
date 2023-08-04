from typing import List

from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

import app.repositories.run_date as run_date_repository
import app.repositories.task as task_repository
import app.repositories.user as user_repository
import app.schemas.schemas as schemas
from app.db.database import Base, engine, get_db

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/sample")
def sample():
    return {"message": "Hello World"}


# Read


@app.get("/users", response_model=List[schemas.User])
def read_users(
        skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = user_repository.get_users(db=db, skip=skip, limit=limit)
    return users


@app.get("/tasks", response_model=List[schemas.Task])
def read_tasks(
        skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    tasks = task_repository.get_tasks(db=db, skip=skip, limit=limit)
    return tasks


@app.get("/rundates", response_model=List[schemas.RunDate])
def read_run_dates(
        skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    run_dates = run_date_repository.get_run_dates(
        db=db, skip=skip, limit=limit)
    return run_dates

# Create


@app.post("/users", response_model=schemas.User)
def create_user(
        user: schemas.UserCreate, db: Session = Depends(get_db)):
    return user_repository.create_user(db=db, user=user)


@app.post("/tasks", response_model=schemas.Task)
def create_task(
        task: schemas.TaskCreate, db: Session = Depends(get_db)):
    return task_repository.create_task(db=db, task=task)


@app.post("/rundates", response_model=schemas.RunDate)
def create_run_date(
        run_date: schemas.RunDateCreate, db: Session = Depends(get_db)):
    return run_date_repository.create_run_date(db=db, run_date=run_date)
