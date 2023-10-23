from app.schemas.core import BaseSchema
import datetime
from pydantic import ConfigDict


class RunDateSchemaBase(BaseSchema):

    model_config = ConfigDict(from_attributes=True)


class RunDateResponse(RunDateSchemaBase):
    id: int
    run_at: datetime.datetime


class RunDateCreate(RunDateSchemaBase):
    pass


class RunDateUpdate(RunDateSchemaBase):
    order_num: int
