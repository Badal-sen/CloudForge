from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import JWTError, jwt
from sqlalchemy.orm import Session

from app.core.config import settings
from app.database.database import SessionLocal
from app.models.user import User

security = HTTPBearer()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db),
):
    print("=" * 60)
    print("HTTPBearer credentials:", credentials)

    token = credentials.credentials
    print("JWT token:", token)

    try:
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM],
        )

        print("Decoded payload:", payload)

        email = payload.get("sub")

        if email is None:
            raise HTTPException(
                status_code=401,
                detail="Invalid token",
            )

    except JWTError as e:
        print("JWT ERROR:", e)
        raise HTTPException(
            status_code=401,
            detail="Invalid token",
        )

    user = db.query(User).filter(
        User.email == email
    ).first()

    print("Database user:", user)

    if user is None:
        raise HTTPException(
            status_code=401,
            detail="User not found",
        )

    print("=" * 60)

    return user