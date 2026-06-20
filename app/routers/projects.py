from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import SessionLocal
from app.dependencies.auth import get_current_user
from app.models.project import Project
from app.models.user import User
from app.schemas.project_schema import (
    ProjectCreate,
    ProjectResponse,
)

router = APIRouter(
    prefix="/projects",
    tags=["Projects"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post(
    "",
    response_model=ProjectResponse,
    status_code=201,
)
def create_project(
    project: ProjectCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    new_project = Project(
        name=project.name,
        description=project.description,
        owner_id=current_user.id,
    )

    db.add(new_project)
    db.commit()
    db.refresh(new_project)

    return new_project


@router.get(
    "",
    response_model=list[ProjectResponse],
)
def get_projects(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return (
        db.query(Project)
        .filter(Project.owner_id == current_user.id)
        .all()
    )


@router.get(
    "/{project_id}",
    response_model=ProjectResponse,
)
def get_project(
    project_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    project = (
        db.query(Project)
        .filter(
            Project.id == project_id,
            Project.owner_id == current_user.id,
        )
        .first()
    )

    if not project:
        raise HTTPException(
            status_code=404,
            detail="Project not found",
        )

    return project


@router.put(
    "/{project_id}",
    response_model=ProjectResponse,
)
def update_project(
    project_id: int,
    project_data: ProjectCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    project = (
        db.query(Project)
        .filter(
            Project.id == project_id,
            Project.owner_id == current_user.id,
        )
        .first()
    )

    if not project:
        raise HTTPException(
            status_code=404,
            detail="Project not found",
        )

    project.name = project_data.name
    project.description = project_data.description

    db.commit()
    db.refresh(project)

    return project


@router.delete("/{project_id}")
def delete_project(
    project_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    project = (
        db.query(Project)
        .filter(
            Project.id == project_id,
            Project.owner_id == current_user.id,
        )
        .first()
    )

    if not project:
        raise HTTPException(
            status_code=404,
            detail="Project not found",
        )

    db.delete(project)
    db.commit()

    return {
        "message": "Project deleted successfully"
    }