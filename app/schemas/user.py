from pydantic import Field
from app.schemas.core import BaseSchema


class UserCreate(BaseSchema):
    name: str = Field(max_length=12)
    email: str
    # FIXME: 12文字までの制限にする（今はハッシュ化した12文字以上の値をreturnしている）
    password: str = Field(max_length=120)


class UserResponse(BaseSchema):
    id: int
    name: str
    email: str

    class Config:
        orm_mode = True
