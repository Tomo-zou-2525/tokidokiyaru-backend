from tests.test_main import client


def test_create_run_date():
    json_data = dict(task_id=2)
    response = client.post("/rundates", json=json_data)
    assert response.status_code == 200
    assert response.json()["date"]  # datetimeは存在するかだけ確認
