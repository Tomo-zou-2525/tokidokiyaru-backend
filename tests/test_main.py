from fastapi.testclient import TestClient

from src.sql_app.main import app

client = TestClient(app)


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
