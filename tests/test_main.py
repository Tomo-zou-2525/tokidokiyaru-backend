import random

from fastapi.testclient import TestClient

from app import main
from app.schemas import schemas

client = TestClient(main.app)


def test_sample():
    response = client.get("/sample")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

# Read


def test_read_users():
    response = client.get("/users")
    assert response.status_code == 200


def test_read_tasks():
    response = client.get("/tasks")
    assert response.status_code == 200


def test_read_run_dates():
    response = client.get("/rundates")
    assert response.status_code == 200

# Create


test_rand_str = "test" + str(random.randint(0, 10000000))


def test_create_user():
    user = schemas.UserCreate(
        name=test_rand_str,
        email=test_rand_str + "@test.com",
        password="test"
    )
    response = client.post("/users", json=user.dict())
    assert response.status_code == 200
    assert response.json()["name"] == test_rand_str
    assert response.json()["email"] == test_rand_str + "@test.com"


def test_create_task():
    rand_int = random.randint(0, 10000000)
    task = schemas.TaskCreate(
        user_id=1,
        name=test_rand_str,
        order=rand_int
    )
    response = client.post("/tasks", json=task.dict())
    assert response.status_code == 200
    assert response.json()["name"] == test_rand_str
    assert response.json()["user_id"] == 1
    assert response.json()["order"] == rand_int


def test_create_run_date():
    json_data = dict(task_id=1)
    response = client.post("/rundates", json=json_data)
    assert response.status_code == 200
    assert response.json()["date"]  # datetimeは存在するかだけ確認
