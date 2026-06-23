from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from datetime import datetime
import platform
import socket

from app.database.database import Base, engine

# Import Models
from app.models.user import User
from app.models.project import Project
from app.models.deployment import Deployment

# Import Routers
from app.routers.auth import router as auth_router
from app.routers.projects import router as projects_router
from app.routers.deployments import router as deployments_router

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="CloudForge DevOps Platform",
    description="""
Production-ready DevOps platform built with:

- FastAPI
- Docker
- AWS EC2
- PostgreSQL (Amazon RDS)
- Application Load Balancer
- GitHub Actions CI/CD
- Cloudflare
- HTTPS
""",
    version="2.0.0",
)

# Register Routers
app.include_router(auth_router)
app.include_router(projects_router)
app.include_router(deployments_router)


@app.get("/", response_class=HTMLResponse, tags=["Home"])
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>CloudForge DevOps Platform</title>

        <style>
            body{
                background:#0f172a;
                color:white;
                font-family:Arial,sans-serif;
                text-align:center;
                padding:60px;
                margin:0;
            }

            .card{
                max-width:850px;
                margin:auto;
                background:#1e293b;
                padding:40px;
                border-radius:15px;
                box-shadow:0 0 25px rgba(0,0,0,.35);
            }

            h1{
                color:#38bdf8;
                margin-bottom:10px;
            }

            h3{
                color:#38bdf8;
                margin-top:35px;
            }

            p{
                font-size:18px;
                line-height:1.6;
            }

            hr{
                border:none;
                border-top:1px solid #334155;
                margin:25px 0;
            }

            .status{
                color:#22c55e;
                font-weight:bold;
            }

            code{
                color:#facc15;
                background:#0f172a;
                padding:2px 6px;
                border-radius:4px;
            }

            a{
                color:#38bdf8;
                text-decoration:none;
            }

            .tech{
                color:#cbd5e1;
            }
        </style>
    </head>

    <body>

        <div class="card">

            <h1>☁️ CloudForge</h1>

            <p>AWS DevOps Automation Platform</p>

            <hr>

            <p>
                Status:
                <span class="status">● ONLINE</span>
            </p>

            <p><strong>Version:</strong> 2.0.0</p>

            <p class="tech">
                FastAPI • Docker • PostgreSQL • AWS EC2 • ALB • Cloudflare • GitHub Actions
            </p>

            <h3>Features</h3>

            <p>✅ JWT Authentication</p>
            <p>✅ Project Management API</p>
            <p>✅ Deployment Management API</p>
            <p>✅ PostgreSQL Database</p>
            <p>✅ Docker Container</p>
            <p>✅ GitHub Actions CI/CD</p>
            <p>✅ HTTPS with Cloudflare</p>
            <p>✅ AWS EC2 + Application Load Balancer</p>

            <h3>Architecture</h3>

            <p>
                Client
                <br>↓
                <br>Cloudflare
                <br>↓
                <br>Application Load Balancer
                <br>↓
                <br>EC2 (Docker + FastAPI)
                <br>↓
                <br>Amazon RDS PostgreSQL
            </p>

            <hr>

            <h3>API Endpoints</h3>

            <p>Health → <code>/health</code></p>

            <p>Version → <code>/version</code></p>

            <p>Info → <code>/info</code></p>

            <p>Swagger Docs → <a href="/docs">/docs</a></p>

        </div>

    </body>
    </html>
    """


@app.get("/health", tags=["System"])
def health():
    return {
        "status": "healthy",
        "application": "CloudForge",
        "version": "2.0.0"
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
        "framework": "FastAPI",
        "cloud": "AWS",
        "runtime": "Docker",
        "hostname": socket.gethostname(),
        "python": platform.python_version(),
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }