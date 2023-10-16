from humps import camel
from pydantic import BaseModel


def to_camel(string: str) -> str:
    return camel.case(string)


class BaseSchema(BaseModel):
    class Config:
        alias_generator = to_camel
        populate_by_name = True
