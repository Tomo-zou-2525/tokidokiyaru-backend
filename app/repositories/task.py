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
    def get_with_dones(self, db, id):
        return db.query(self.model).filter(self.model.id == id).join(Task.dones).first()


task = CRUDTask(model=Task)
