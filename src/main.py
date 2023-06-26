from fastapi import FastAPI

app = FastAPI()


@app.get("/test")
def test():
    return {"message": "Hello World"}


@app.get("/tasks/{id}")
def task_test(id: int):
    # 処理
    tasks = {
        "tasks": [
            {
                "id": 1,
                "name": "そうじ",
            },
            {
                "id": 2,
                "name": "洗濯",
            },
            {
                "id": 3,
                "name": {id},
            }
        ]
    }

    return tasks
