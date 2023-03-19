from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps
from app.models.user import User
from app.core.auth import authenticate, create_access_token


router = APIRouter()

@router.post("/login", status_code=200)
def login(db: Session = Depends(deps.get_db), form_data: OAuth2PasswordRequestForm = Depends()) -> Any:
    user = authenticate(email=form_data.username, password=form_data.password, db=db)
    if not user:
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    return {"access_token": create_access_token(sub=user.id), "token_type": "bearer"}


@router.post("/register", response_model=schemas.User, status_code=201)
def register(*, db: Session = Depends(deps.get_db), user: schemas.UserCreate) -> Any:
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="User already exists")
        
    user = crud.user.create(db=db, obj_in=user)
    return user

@router.get("/me", response_model=schemas.User)
def get_current_user(current_user: User = Depends(deps.get_current_user)) -> Any:
    return current_user
