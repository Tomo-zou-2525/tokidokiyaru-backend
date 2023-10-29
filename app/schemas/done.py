from app.schemas.core import BaseSchema
from pydantic import ConfigDict
import datetime


class DoneSchemaBase(BaseSchema):

    model_config = ConfigDict(from_attributes=True)


class DoneCreate(DoneSchemaBase):
    task_id: int


# TaskResponseに含めるのでtask_idは不要
class DoneResponse(DoneSchemaBase):
    id: int
    done_at: datetime.datetime
