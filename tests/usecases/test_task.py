from random import randint

from faker import Faker

from app.schemas.task import TaskCreate
from tests.test_main import client

fake = Faker('ja_JP')


def test_read_tasks():
    response = client.get("/tasks")
    assert response.status_code == 200


def test_create_task():
    task = TaskCreate(
        user_id=1,
        name=fake.job() + 'の勉強',
        order=randint(0, 10000000)
    )
    response = client.post("/tasks", json=task.dict())
    assert response.status_code == 200
    assert response.json()["user_id"] == task.user_id
    assert response.json()["name"] == task.name
    assert response.json()["order"] == task.order
