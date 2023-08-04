
import random

from app.schemas.task import TaskCreate
from tests.test_main import client


def test_read_tasks():
    response = client.get("/tasks")
    assert response.status_code == 200


test_rand_str = "test" + str(random.randint(0, 10000000))


def test_create_task():
    rand_int = random.randint(0, 10000000)
    task = TaskCreate(
        user_id=1,
        name=test_rand_str,
        order=rand_int
    )
    response = client.post("/tasks", json=task.dict())
    assert response.status_code == 200
    assert response.json()["name"] == test_rand_str
    assert response.json()["user_id"] == 1
    assert response.json()["order"] == rand_int
