from fastapi.testclient import TestClient

from src.sql_app.main import app

client = TestClient(app)


def test_sample():
    response = client.get("/sample")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}
