from fastapi import FastAPI
from app.controllers.homeworks import router as HomeworkController
import fastapi.middleware.cors as cors

app = FastAPI()

origins = ["*"]

app.add_middleware(
    cors.CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(HomeworkController, tags=["Homeworks"], prefix="/homeworks")


@app.get("/", tags=["API Root"])
async def read_root():
    return {"message": "Welcome to homeworksAPI"}
