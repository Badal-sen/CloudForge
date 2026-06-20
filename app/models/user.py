from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from app.database.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    full_name = Column(String, nullable=False)

    email = Column(String, unique=True, nullable=False)

    password = Column(String, nullable=False)

    role = Column(String, default="Developer")

    created_at = Column(DateTime, default=datetime.utcnow)

    projects = relationship(
        "Project",
        back_populates="owner",
        cascade="all, delete"
    )