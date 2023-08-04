import datetime

from pydantic import BaseModel, Field


class RunDateCreate(BaseModel):
    task_id: int
    date: datetime.datetime = Field(default_factory=datetime.datetime.now)


class RunDateResponse(RunDateCreate):
    id: int

    class Config:
        orm_mode = True
