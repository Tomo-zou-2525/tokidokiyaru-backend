import datetime

from pydantic import BaseModel, Field


class UserCreate(BaseModel):
    name: str = Field(max_length=12)
    email: str
    password: str = Field(max_length=12)


class User(UserCreate):
    id: int

    class Config:
        orm_mode = True


class TaskCreate(BaseModel):
    user_id: int
    name: str = Field(max_length=12)
    order: int


class Task(TaskCreate):
    id: int

    class Config:
        orm_mode = True


class RunDateCreate(BaseModel):
    task_id: int
    date: datetime.datetime = Field(default_factory=datetime.datetime.now)


class RunDate(RunDateCreate):
    id: int

    class Config:
        orm_mode = True
