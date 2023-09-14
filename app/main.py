from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.usecases.run_date import router as run_date_router
from app.usecases.task import router as task_router
from app.usecases.user import router as user_router

app = FastAPI()
app.include_router(user_router)
app.include_router(task_router)
app.include_router(run_date_router)

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
