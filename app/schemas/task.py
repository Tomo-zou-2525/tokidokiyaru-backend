from pydantic import Field, ConfigDict

from app.schemas.core import BaseSchema


class TaskSchemaBase(BaseSchema):
    user_id: int
    name: str = Field(max_length=12)

    model_config = ConfigDict(from_attributes=True)


class TaskResponse(TaskSchemaBase):
    id: int
    order_num: int


class TaskCreate(TaskSchemaBase):
    pass


class TaskUpdate(TaskSchemaBase):
    order_num: int


# from typing import List

# from pydantic import Field
# from app.schemas.core import BaseSchema

# from app.schemas.done import DoneResponse


# class TaskCreate(BaseSchema):
#     user_id: int
#     name: str = Field(max_length=12)
#     order: int


# class TaskResponse(BaseSchema):
#     id: int
#     user_id: int
#     name: str
#     ran_at: List[DoneResponse]
#     order: int

#     class Config:
#         orm_mode = True
