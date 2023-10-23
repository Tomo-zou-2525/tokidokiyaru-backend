from tests.test_main import client

endpoint = "users"


def test_create_user():
    response = client.post(
        f"/{endpoint}/",
        json={"name": "テストユーザー", "email": "sample@example.com", "password": "test"},
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert "id" in data
    id = data["id"]

    response = client.get(f"/{endpoint}/{id}")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["id"] == id
    assert data["name"] == "テストユーザー"
    assert data["email"] == "sample@example.com"
