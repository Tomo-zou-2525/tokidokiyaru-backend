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
    def get_with_dones(self, db, task_id):
        return db.query(self.model).filter(self.model.id == task_id).join(Task.dones).first()

    def get_user_task_list_with_dones(self, db, user_id):
        return db.query(self.model).filter(self.model.user_id == user_id).join(Task.dones).all()


task = CRUDTask(model=Task)
