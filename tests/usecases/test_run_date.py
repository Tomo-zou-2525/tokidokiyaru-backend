from tests.test_main import client

endpoint = "rundates"


def test_create_rundate():
    # ユーザー作成
    response = client.post(
        "/users/",
        json={"name": "テストユーザー３",
              "email": "sample3@example.com", "password": "test3"},
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert "id" in data
    user_id = data["id"]
    # タスク作成
    response = client.post(
        "/tasks/",
        json={"userId": user_id, "name": "テストタスク"},
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert "id" in data
    task_id = data["id"]
    # 実施日作成
    response = client.post(
        f"/{endpoint}/",
        json={"taskId": task_id},
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert "id" in data
    assert data["taskId"] == task_id
    assert "runAt" in data
