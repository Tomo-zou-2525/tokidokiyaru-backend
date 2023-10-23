from tests.test_main import client

endpoint = "tasks"


def test_create_task():
    response = client.post(
        "/users/",
        json={"name": "テストユーザー２",
              "email": "sample2@example.com", "password": "test2"},
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert "id" in data
    user_id = data["id"]

    response = client.post(
        f"/{endpoint}/",
        json={"userId": user_id, "name": "テストタスク"},
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert "id" in data
    task_id = data["id"]

    response = client.get(f"/{endpoint}/{task_id}")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["id"] == task_id
    assert data["userId"] == user_id
    assert data["name"] == "テストタスク"
