from app.schemas.core import BaseSchema
from pydantic import ConfigDict
import datetime


class DoneSchemaBase(BaseSchema):

    model_config = ConfigDict(from_attributes=True)


# TaskResponseに含めるのでtask_idは不要
class DoneResponse(DoneSchemaBase):
    id: int
    done_at: datetime.datetime


class DoneCreate(DoneSchemaBase):
    task_id: int


# 使わない
class DoneUpdate(DoneSchemaBase):
    pass
