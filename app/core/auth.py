from typing import List, Union, Optional, MutableMapping

from datetime import datetime, timedelta

from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from sqlalchemy.orm import Session

from app.models.user import User
from app.core.security import get_password_hash, verify_password
from app.core.config import settings

JWTPayloadMapping = MutableMapping[
    str, Union[datetime, bool, str, List[str], List[int]]
]

oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f"{settings.API_V1_STR}/auth/login")

def authenticate(*, email: str, password: str, db: Session) -> Optional[User]:
    user = db.query(User).filter(User.email == email).first()
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user


def create_access_token(*, sub: str) -> str:
   return create_token(
    token_type="access_token",
    lifetime=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES),
    sub=sub
   )

def create_token(token_type: str, lifetime: timedelta, sub: str) -> str:
    payload = {}
    expire = datetime.utcnow() + lifetime
    payload["sub"] = str(sub)
    payload["token_type"] = token_type
    payload["exp"] = expire
    payload["iat"] = datetime.utcnow()
    return jwt.encode(payload, settings.JWT_SECRET_KEY, algorithm=settings.ALGORITHM)
