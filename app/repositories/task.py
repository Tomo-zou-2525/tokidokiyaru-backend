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
    def get_task_list(self, db):
        return db.query(self.model).all()


task = CRUDTask(model=Task)
