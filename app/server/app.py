from fastapi import FastAPI

from server.routes.student import router as StudentRouter
from server.routes.task import router as TaskRouter

app = FastAPI()

app.include_router(StudentRouter, tags=["Student"], prefix="/student")
app.include_router(TaskRouter, tags=["Task"], prefix="/task")


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}
