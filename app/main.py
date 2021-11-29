from fastapi import FastAPI
from app.controllers.homeworks import router as HomeworkController

app = FastAPI()

app.include_router(HomeworkController, tags=["Homewrks"], prefix="/homeworks")


@app.get("/", tags=["API Root"])
async def read_root():
    return {"message": "Welcome to homeworksAPI"}
