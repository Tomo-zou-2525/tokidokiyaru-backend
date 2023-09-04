
from faker import Faker

from app.schemas.user import UserCreate
from tests.test_main import client

fake = Faker('ja_JP')


def test_read_users():
    response = client.get("/users")
    assert response.status_code == 200


def test_create_user():
    user = UserCreate(
        name=fake.name(),
        email=fake.email(),
        password="test"
    )
    response = client.post("/users", json=user.dict())
    assert response.status_code == 200
    assert response.json()["name"] == user.name
    assert response.json()["email"] == user.email
