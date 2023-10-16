from typing import List

from pydantic import Field
from app.schemas.core import BaseSchema

from app.schemas.run_date import RunDateResponse


class TaskCreate(BaseSchema):
    user_id: int
    name: str = Field(max_length=12)
    order: int


class TaskResponse(BaseSchema):
    id: int
    user_id: int
    name: str
    rundates: List[RunDateResponse]
    order: int

    class Config:
        orm_mode = True
