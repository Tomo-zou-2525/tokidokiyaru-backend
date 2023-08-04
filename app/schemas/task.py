from pydantic import BaseModel, Field


class TaskCreate(BaseModel):
    user_id: int
    name: str = Field(max_length=12)
    order: int


class TaskResponse(TaskCreate):
    id: int

    class Config:
        orm_mode = True
