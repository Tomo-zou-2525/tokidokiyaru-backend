from typing import Optional

from app.schemas.core import BaseSchema
from pydantic import Field, ConfigDict


class UserSchemaBase(BaseSchema):
    name: str = Field(max_length=12)
    email: Optional[str] = Field(max_length=255)

    model_config = ConfigDict(from_attributes=True)


class UserResponse(UserSchemaBase):
    id: int


class UserCreate(UserSchemaBase):
    password: Optional[str] = Field(max_length=120)


class UserUpdate(UserSchemaBase):
    password: Optional[str] = Field(max_length=120)
