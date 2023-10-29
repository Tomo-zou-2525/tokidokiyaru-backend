from app.schemas.core import BaseSchema
import datetime
from pydantic import ConfigDict


class DoneSchemaBase(BaseSchema):
    task_id: int

    model_config = ConfigDict(from_attributes=True)


class DoneResponse(DoneSchemaBase):
    id: int
    done_at: datetime.datetime


class DoneCreate(DoneSchemaBase):
    pass


class DoneUpdate(DoneSchemaBase):
    order_num: int
