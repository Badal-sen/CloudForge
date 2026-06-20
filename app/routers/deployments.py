from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import SessionLocal
from app.dependencies.auth import get_current_user

from app.models.user import User
from app.models.project import Project
from app.models.deployment import Deployment

from app.schemas.deployment_schema import (
    DeploymentCreate,
    DeploymentResponse,
)

router = APIRouter(
    prefix="/deployments",
    tags=["Deployments"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post(
    "",
    response_model=DeploymentResponse,
    status_code=201,
)
def create_deployment(
    deployment: DeploymentCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    project = (
        db.query(Project)
        .filter(
            Project.id == deployment.project_id,
            Project.owner_id == current_user.id,
        )
        .first()
    )

    if not project:
        raise HTTPException(
            status_code=404,
            detail="Project not found",
        )

    new_deployment = Deployment(
        version=deployment.version,
        environment=deployment.environment,
        status="Pending",
        project_id=deployment.project_id,
    )

    db.add(new_deployment)
    db.commit()
    db.refresh(new_deployment)

    return new_deployment


@router.get(
    "",
    response_model=list[DeploymentResponse],
)
def get_deployments(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return (
        db.query(Deployment)
        .join(Project)
        .filter(Project.owner_id == current_user.id)
        .all()
    )


@router.get(
    "/{deployment_id}",
    response_model=DeploymentResponse,
)
def get_deployment(
    deployment_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    deployment = (
        db.query(Deployment)
        .join(Project)
        .filter(
            Deployment.id == deployment_id,
            Project.owner_id == current_user.id,
        )
        .first()
    )

    if not deployment:
        raise HTTPException(
            status_code=404,
            detail="Deployment not found",
        )

    return deployment


@router.put(
    "/{deployment_id}",
    response_model=DeploymentResponse,
)
def update_deployment(
    deployment_id: int,
    deployment_data: DeploymentCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    deployment = (
        db.query(Deployment)
        .join(Project)
        .filter(
            Deployment.id == deployment_id,
            Project.owner_id == current_user.id,
        )
        .first()
    )

    if not deployment:
        raise HTTPException(
            status_code=404,
            detail="Deployment not found",
        )

    deployment.version = deployment_data.version
    deployment.environment = deployment_data.environment
    deployment.project_id = deployment_data.project_id

    db.commit()
    db.refresh(deployment)

    return deployment


@router.delete("/{deployment_id}")
def delete_deployment(
    deployment_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    deployment = (
        db.query(Deployment)
        .join(Project)
        .filter(
            Deployment.id == deployment_id,
            Project.owner_id == current_user.id,
        )
        .first()
    )

    if not deployment:
        raise HTTPException(
            status_code=404,
            detail="Deployment not found",
        )

    db.delete(deployment)
    db.commit()

    return {
        "message": "Deployment deleted successfully"
    }