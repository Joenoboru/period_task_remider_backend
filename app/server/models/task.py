from typing import Optional

from pydantic import BaseModel, Field


class TaskSchema(BaseModel):
    task: str = Field(...)
    reminder_cycle: int = Field(default=7)
    dayCount: int = Field(default=0)

    class Config:
        json_schema_extra = {
            "example": {
                "task": "Change toothbrush",
                "reminder_cycle": 90,
                "dayCount": 0,
            }
        }


class UpdateTaskModel(BaseModel):
    task: Optional[str]
    reminder_cycle: Optional[str]
    dayCount: Optional[int]

    class Config:
        json_schema_extra = {
            "example": {
                "task": "Change toothbrush",
                "reminder_cycle": 90,
                "dayCount": 0,
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
