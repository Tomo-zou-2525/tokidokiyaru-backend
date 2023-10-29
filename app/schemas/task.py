from typing import List
from pydantic import Field, ConfigDict
from app.schemas.core import BaseSchema
from app.schemas.done import DoneResponse


class TaskSchemaBase(BaseSchema):

    model_config = ConfigDict(from_attributes=True)


class TaskResponse(TaskSchemaBase):
    id: int
    user_id: int
    name: str = Field(max_length=20)
    order_num: int
    dones: List[DoneResponse]


class TaskCreate(TaskSchemaBase):
    user_id: int
    name: str = Field(max_length=20)


class TaskUpdate(TaskSchemaBase):
    id: int
    name: str | None = Field(max_length=20)
    order_num: int | None
