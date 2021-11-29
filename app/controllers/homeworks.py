from typing import List
from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from app.database import (
    retrieve_homeworks,
    retrieve_homework,
    insert_homework,
    update_homework,
    remove_homework
)

from app.models.homeworks import (
    HomeworkModel,
    UpdateHomeworkModel
)

router = APIRouter()

@router.get("/", response_description="Get Homeworks", response_model=List[HomeworkModel])
async def get_ufos():
    homeworks = await retrieve_homeworks()
    if homeworks:
        return homeworks
    return "Empty list returned"

@router.get("/{id}", response_description="Get Homework by ID")
async def get_ufo(homework_id):
    homework = await retrieve_homework(homework_id)
    print(homework)
    if homework:
        return homework
    return "UFO doesn't exist"


@router.post("/", response_description="Homework data added into the database", response_model=HomeworkModel)
async def post_ufo(homework: HomeworkModel = Body(...)):
    homework = jsonable_encoder(homework)
    new_homework = await insert_homework(homework)
    return new_homework


@router.put("/{id}")
async def put_ufo(homework_id: str, req: UpdateHomeworkModel= Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_homework = await update_homework(homework_id, req)
    if updated_homework:
        return updated_homework
    return "There was an error updating UFO data"

@router.delete("/{id}", response_description="Homework data deleted from the database")
async def delete_ufo(homework_id: str):
    deleted_homework = await remove_homework(homework_id)
    if deleted_homework:
        return f"Homework with ID: {homework_id} removed successfully"

    return f"Homework with id {homework_id} doesn't exist"
