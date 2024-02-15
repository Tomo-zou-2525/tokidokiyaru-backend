from tests.test_main import client

endpoint = 'tasks'


def test_create_task():
    response = client.post(
        f"/{endpoint}/",
        json={"name": "テストタスク"},
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert "id" in data
    task_id = data["id"]

    response = client.get(f"/{endpoint}/{task_id}")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["id"] == task_id
    assert data["name"] == "テストタスク"
