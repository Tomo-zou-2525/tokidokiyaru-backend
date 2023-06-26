import datetime

from pydantic import BaseModel, Field


class User(BaseModel):
    id: int
    name: str = Field(max_length=12)
    email: str
    password: str = Field(max_length=12)

    class Config:
        orm_mode = True


class Task(BaseModel):
    id: int
    user_id: int
    name: str = Field(max_length=12)
    order: int

    class Config:
        orm_mode = True


class RunDate(BaseModel):
    id: int
    task_id: int
    date: datetime.datetime = Field(default_factory=datetime.datetime.now)

    class Config:
        orm_mode = True
