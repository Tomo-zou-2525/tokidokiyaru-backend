
import random

from app.schemas.user import UserCreate
from tests.test_main import client


def test_read_users():
    response = client.get("/users")
    assert response.status_code == 200


test_rand_str = "test" + str(random.randint(0, 10000000))


def test_create_user():
    user = UserCreate(
        name=test_rand_str,
        email=test_rand_str + "@test.com",
        password="test"
    )
    response = client.post("/users", json=user.dict())
    assert response.status_code == 200
    assert response.json()["name"] == test_rand_str
    assert response.json()["email"] == test_rand_str + "@test.com"
