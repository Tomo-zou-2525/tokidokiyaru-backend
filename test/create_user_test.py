import json
import random

import requests
from faker import Faker

url = "http://localhost:8000/users"

name = Faker().name()[:12]
email = Faker().email()
password = "password" + str(random.randint(1, 999))

data = {
    "name": name,
    "email": email,
    "password": password
}
json_data = json.dumps(data)

response = requests.post(url, data=json_data, headers={
                         "Content-Type": "application/json"})

if response.status_code == 200:
    print("リクエストに成功しました。ステータスコード:", response.status_code)
    print(response.json())
else:
    print("リクエストに失敗しました。ステータスコード:", response.status_code)
    print(response.text)
