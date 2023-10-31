import hashlib
from fastapi import APIRouter
from datetime import datetime
from app.db.session import SessionLocal
from app.models.done import Done
from app.models.task import Task
from app.models.user import User

router = APIRouter()


@router.post("/seeder")
def seeder():
    db = SessionLocal()
    users = [
        User(
            id=1,
            name="user1",
            email="user1@user1.com",
            password=hashlib.sha256(b"user1").hexdigest(),
        ),
        User(
            id=2,
            name="user2",
            email="user2@user2.com",
            password=hashlib.sha256(b"user2").hexdigest(),
        ),
        User(
            id=3,
            name="user3",
            email="user3@user3.com",
            password=hashlib.sha256(b"user3").hexdigest(),
        ),
    ]
    db.add_all(users)
    db.commit()

    # Create Tasks
    tasks = [
        Task(id=1, user_id=1, name="オイル交換", order_num=1),
        Task(id=2, user_id=1, name="スマホ契約プランの見直し", order_num=2),
        Task(id=3, user_id=1, name="散髪", order_num=3),
        Task(id=4, user_id=2, name="自転車点検", order_num=4),
        Task(id=5, user_id=3, name="ふとんクリーニング", order_num=5),
    ]
    db.add_all(tasks)
    db.commit()

    # # Create Dones
    dones = [
        Done(id=1, task_id=1, done_at=datetime(2021, 4, 1, 11, 30)),
        Done(id=2, task_id=2, done_at=datetime(2021, 5, 1, 14, 20)),
        Done(id=3, task_id=3, done_at=datetime(2021, 3, 1, 16, 5)),
        Done(id=4, task_id=3, done_at=datetime(2021, 4, 1, 16, 11)),
        Done(id=5, task_id=3, done_at=datetime(2021, 5, 1, 16, 45)),
        Done(id=6, task_id=4, done_at=datetime(2022, 11, 16, 17, 0)),
        Done(id=7, task_id=5, done_at=datetime(2023, 10, 29, 9, 30)),
    ]
    db.add_all(dones)
    db.commit()
