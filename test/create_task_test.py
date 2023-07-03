import json
import random

import requests
from faker import Faker

url = "http://localhost:8000/tasks"

user_id = random.randint(1, 1)
name = Faker().word()[:12]
order = random.randint(1, 99999)

data = {
    "user_id": user_id,
    "name": name,
    "order": order
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
