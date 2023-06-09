import hashlib
from datetime import datetime

from database import SessionLocal
from models import RunDate, Task, User

db = SessionLocal()


def seed():
    # Create Users
    users = [
        User(
            id=1,
            name="user1",
            email="user1@example.com",
            password=hashlib.sha256(b"user1").hexdigest()),
        User(
            id=2,
            name="user2",
            email="user2@user2.com",
            password=hashlib.sha256(b"user2").hexdigest()),
        User(
            id=3,
            name="user3",
            email="user3@user3.com",
            password=hashlib.sha256(b"user3").hexdigest()),
    ]
    db.add_all(users)
    db.commit()

    # Create Tasks
    tasks = [
        Task(id=1, user_id=1, name="オイル交換", order=1),
        Task(id=2, user_id=1, name="スマホ契約プランの見直し", order=2),
        Task(id=3, user_id=1, name="散髪", order=3),
        Task(id=4, user_id=2, name="自転車点検", order=1),
        Task(id=5, user_id=3, name="ふとんクリーニング", order=1),
    ]
    db.add_all(tasks)
    db.commit()

    # # Create RunDates
    run_dates = [
        RunDate(id=1, task_id=1, date=datetime(2021, 4, 1, 11, 30)),
        RunDate(id=2, task_id=2, date=datetime(2021, 5, 1, 14, 20)),
        RunDate(id=3, task_id=3, date=datetime(2021, 3, 1, 16, 5)),
        RunDate(id=4, task_id=3, date=datetime(2021, 4, 1, 16, 11)),
        RunDate(id=5, task_id=3, date=datetime(2021, 5, 1, 16, 45)),
        RunDate(id=6, task_id=4, date=datetime(2022, 11, 16, 17, 0)),
        RunDate(id=7, task_id=5, date=datetime(2023, 10, 29, 9, 30)),
    ]
    db.add_all(run_dates)
    db.commit()


if __name__ == '__main__':
    BOS = '\033[92m'  # 緑色表示用
    EOS = '\033[0m'

    print(f'{BOS}Seeding data...{EOS}')
    seed()
