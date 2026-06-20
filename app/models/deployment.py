from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from app.database.database import Base


class Deployment(Base):
    __tablename__ = "deployments"

    id = Column(Integer, primary_key=True, index=True)

    version = Column(String, nullable=False)

    environment = Column(String, nullable=False)

    status = Column(String, default="Pending")

    deployed_at = Column(DateTime, default=datetime.utcnow)

    project_id = Column(Integer, ForeignKey("projects.id"))

    project = relationship("Project", back_populates="deployments")