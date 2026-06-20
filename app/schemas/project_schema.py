from pydantic import BaseModel
from datetime import datetime


class ProjectCreate(BaseModel):
    name: str
    description: str


class ProjectResponse(BaseModel):
    id: int
    name: str
    description: str
    owner_id: int
    created_at: datetime

    class Config:
        from_attributes = True