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


from datetime import datetime
from fastapi.responses import HTMLResponse


@app.get("/", response_class=HTMLResponse, tags=["Home"])
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>CloudForge</title>
        <style>
            body{
                background:#0f172a;
                color:white;
                font-family:Arial,sans-serif;
                text-align:center;
                padding-top:70px;
            }
            .card{
                width:700px;
                margin:auto;
                background:#1e293b;
                padding:40px;
                border-radius:15px;
                box-shadow:0 0 25px rgba(0,0,0,.35);
            }
            h1{
                color:#38bdf8;
            }
            p{
                font-size:18px;
            }
            .status{
                color:#22c55e;
                font-weight:bold;
            }
            code{
                color:#facc15;
            }
        </style>
    </head>

    <body>

    <div class="card">

    <h1>☁️ CloudForge</h1>

    <p>
    AWS DevOps Automation Platform
    </p>

    <hr>

    <p>Status:
    <span class="status">● ONLINE</span>
    </p>

    <p>Version 2.0</p>

    <p>FastAPI • Docker • AWS EC2 • ALB • Cloudflare • GitHub Actions</p>

    <br>

    <p>
    Health →
    <code>/health</code>
    </p>

    <p>
    API Docs →
    <code>/docs</code>
    </p>

    </div>

    </body>
    </html>
    """


@app.get("/health", tags=["System"])
def health():
    return {
        "status": "healthy",
        "application": "CloudForge",
        "version": "2.0"
    }


@app.get("/version", tags=["System"])
def version():
    return {
        "version": "2.0.0",
        "environment": "Production"
    }


@app.get("/info", tags=["System"])
def info():
    return {
        "project": "CloudForge",
        "domain": "https://badalbk.dev",
        "cloud": "AWS",
        "runtime": "Docker",
        "framework": "FastAPI",
        "deployed_at": datetime.utcnow().isoformat() + "Z"
    }


@app.get("/health", tags=["System"])
def health():
    return {
        "status": "healthy",
        "application": "CloudForge",
        "version": "2.0"
    }

@app.get("/version", tags=["System"])
def version():
    return {
        "version": "2.0.0",
        "environment": "Production"
    }


from datetime import datetime
import platform
import socket

@app.get("/info", tags=["System"])
def info():
    return {
        "project": "CloudForge",
        "domain": "https://badalbk.dev",
        "framework": "FastAPI",
        "cloud": "AWS",
        "runtime": "Docker",
        "hostname": socket.gethostname(),
        "python": platform.python_version(),
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }


