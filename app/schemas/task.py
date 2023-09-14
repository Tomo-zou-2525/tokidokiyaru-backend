from typing import List

from pydantic import BaseModel, Field

from .run_date import RunDateResponse


class TaskCreate(BaseModel):
    user_id: int
    name: str = Field(max_length=12)
    order: int


class TaskResponse(BaseModel):
    id: int
    user_id: int
    name: str
    rundates: List[RunDateResponse]
    order: int

    class Config:
        orm_mode = True
