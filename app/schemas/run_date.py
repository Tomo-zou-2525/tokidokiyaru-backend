import datetime

from pydantic import Field
from app.schemas.core import BaseSchema


class RunDateCreate(BaseSchema):
    task_id: int
    date: datetime.datetime = Field(default_factory=datetime.datetime.now)


class RunDateResponse(BaseSchema):
    date: datetime.datetime = Field(default_factory=datetime.datetime.now)

    class Config:
        orm_mode = True
