from fastapi import APIRouter
from app.models.project import Project
from app.database import projects

router = APIRouter(
    prefix="/projects",
    tags=["Projects"]
)

@router.get("/")
def get_projects():
    return projects

@router.post("/")
def create_project(project: Project):
    projects.append(project)
    return {
        "message": "Project created",
        "project": project
    }

@router.delete("/{project_id}")
def delete_project(project_id: int):

    for p in projects:
        if p.id == project_id:
            projects.remove(p)
            return {"message":"Deleted"}

    return {"message":"Not found"}