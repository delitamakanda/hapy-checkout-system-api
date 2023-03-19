from typing import Generator, Optional

from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session
from jose import jwt, JWTError
from pydantic import BaseModel

from app.db.session import SessionLocal

from app.core.config import settings
from app.models.user import User
from app.core.auth import get_password_hash, verify_password, oauth2_scheme

class Token(BaseModel):
    username: Optional[str] = None

def get_db() -> Generator:
    db = SessionLocal()
    db.current_user_id = None
    try:
        yield db
    finally:
        db.close()


async def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=settings.ALGORITHM, options={"verify_aud": False})
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token = Token(username=username)
    except JWTError:
        raise credentials_exception
    user = db.query(User).filter(User.id == token.username).first()
    if user is None:
        raise credentials_exception
    return user