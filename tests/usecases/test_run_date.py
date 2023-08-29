import random

from tests.test_main import client


def test_read_run_dates():
    response = client.get("/rundates")
    assert response.status_code == 200


test_rand_str = "test" + str(random.randint(0, 10000000))


def test_create_run_date():
    json_data = dict(task_id=2)
    response = client.post("/rundates", json=json_data)
    assert response.status_code == 200
    assert response.json()["date"]  # datetimeは存在するかだけ確認
