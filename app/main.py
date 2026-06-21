from fastapi import FastAPI

from app.database.database import Base, engine

# Import Models
from app.models.user import User
from app.models.project import Project
from app.models.deployment import Deployment

# Import Routers
from app.routers.auth import router as auth_router
from app.routers.projects import router as projects_router
from app.routers.deployments import router as deployments_router

# Create all database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="CloudForge API",
    version="1.0.0",
)

# Register Routers
app.include_router(auth_router)
app.include_router(projects_router)
app.include_router(deployments_router)


@app.get("/", tags=["Home"])
def home():
    return {
        "message": "CloudForge CI/CD Working 🚀 Version 2"
    }