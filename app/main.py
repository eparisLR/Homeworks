from fastapi import FastAPI

app = FastAPI()

@app.get("/", tags=["API Root"])
async def read_root():
    return {"message": "Welcome to homeworksAPI"}
