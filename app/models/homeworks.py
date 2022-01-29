from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field
from bson.objectid import ObjectId


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, value):
        if not ObjectId.is_valid(value):
            raise ValueError("Invalid objectid")
        return ObjectId(value)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")

class HomeworkModel(BaseModel):
    id: Optional[PyObjectId] = Field(default_factory=PyObjectId, alias="_id")
    work_id: int
    deadline: datetime
    tags: List[str]
    is_done: bool
    work: str
    user_id: int 

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "work_id": 1,
                "deadline": "2019-03-22T18:30:00",
                "work": "work1",
                "is_done": False,
                "tags":["exemple"],
                "user_id": 1,
            }
        }

class UpdateHomeworkModel(BaseModel):
    id: Optional[PyObjectId] = Field(default_factory=PyObjectId, alias="_id")
    work_id: Optional[int]
    deadline: Optional[datetime]
    tags: Optional[List[str]]
    is_done: Optional[bool]
    work: Optional[str]
    user_id: Optional[int]

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "work_id": 1,
                "deadline": "2019-03-22T18:30:00",
                "is_done": False,
                "tags":["exemple"],
                "work": "work1",
                "user_id": 1,
            }
        }

class CreateHomeworkModel(BaseModel):
    work_id: Optional[int]
    deadline: Optional[datetime]
    tags: Optional[List[str]]
    is_done: Optional[bool]
    work: Optional[str]
    user_id: Optional[int]

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "work_id": 1,
                "deadline": "2019-03-22T18:30:00",
                "is_done": False,
                "tags":["exemple"],
                "work": "work1",
                "user_id": 1,
            }
        }
