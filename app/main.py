from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.usecases.done import router as done_router
from app.usecases.task import router as task_router
from app.usecases.user import router as user_router
from app.db.seeder import router as seeder_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/sample")
def sample():
    return {"message": "Hello World"}


app.include_router(user_router, prefix="/users")
app.include_router(task_router, prefix="/tasks")
app.include_router(done_router, prefix="/dones")
app.include_router(seeder_router)
