from app.schemas.core import BaseSchema
from pydantic import Field, ConfigDict


class UserSchemaBase(BaseSchema):
    name: str = Field(max_length=12, examples=["テストユーザー"])
    email: str | None = Field(max_length=255, examples=["sample@example.com"])

    model_config = ConfigDict(from_attributes=True)


class UserResponse(UserSchemaBase):
    id: int


class UserCreate(UserSchemaBase):
    password: str | None = Field(max_length=120)


class UserUpdate(UserSchemaBase):
    email: str | None = Field(None, max_length=255, examples=["sample@example.com"])
    password: str | None = Field(None, max_length=120)
