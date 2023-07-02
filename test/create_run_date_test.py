import datetime
import json
import random

import requests

url = "http://localhost:8000/rundates"

task_id = random.randint(1, 1)
date = datetime.datetime.now()

data = {
    "task_id": task_id,
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
