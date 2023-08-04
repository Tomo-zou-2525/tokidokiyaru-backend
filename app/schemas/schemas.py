import datetime

from pydantic import BaseModel, Field


class UserCreate(BaseModel):
    name: str = Field(max_length=12)
    email: str
    # FIXME: 12文字までの制限にする（今はハッシュ化した12文字以上の値をreturnしている）
    password: str = Field(max_length=120)


class UserResponse(UserCreate):
    id: int

    class Config:
        orm_mode = True


class TaskCreate(BaseModel):
    user_id: int
    name: str = Field(max_length=12)
    order: int


class TaskResponse(TaskCreate):
    id: int

    class Config:
        orm_mode = True


class RunDateCreate(BaseModel):
    task_id: int
    date: datetime.datetime = Field(default_factory=datetime.datetime.now)


class RunDateResponse(RunDateCreate):
    id: int

    class Config:
        orm_mode = True
