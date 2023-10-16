from pydantic import Field
from app.schemas.core import BaseSchema


class TaskSchemaBase(BaseSchema):
    user_id: int
    name: str = Field(max_length=12)

    class Config:
        from_attributes = True


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

# from app.schemas.run_date import RunDateResponse


# class TaskCreate(BaseSchema):
#     user_id: int
#     name: str = Field(max_length=12)
#     order: int


# class TaskResponse(BaseSchema):
#     id: int
#     user_id: int
#     name: str
#     ran_at: List[RunDateResponse]
#     order: int

#     class Config:
#         orm_mode = True
