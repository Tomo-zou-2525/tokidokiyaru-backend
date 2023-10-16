from app.models.task import Task
from app.repositories.base import CRUDBase
from app.schemas.task import (
    TaskCreate,
    TaskUpdate,
)


class CRUDTask(
    CRUDBase[
        Task,
        TaskCreate,
        TaskUpdate,
    ]
):
    pass


task = CRUDTask(model=Task)
