from pydantic import BaseModel
from datetime import datetime


class DeploymentCreate(BaseModel):
    version: str
    environment: str
    project_id: int


class DeploymentResponse(BaseModel):
    id: int
    version: str
    environment: str
    status: str
    project_id: int
    deployed_at: datetime

    class Config:
        from_attributes = True