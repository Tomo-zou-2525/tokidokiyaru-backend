from tests.test_main import client

endpoint = 'dones'


def test_create_done():
    # タスク作成
    response = client.post(
        "/tasks/",
        json={"name": "テストタスク"},
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
    assert data["id"] == task_id
    assert "dones" in data
