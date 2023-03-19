from fastapi import FastAPI, APIRouter, Query, HTTPException, Request, Depends
from typing import Optional, Any
from sqlalchemy.orm import Session

from app.schemas.user import User, UserCreate, UserUpdate
from app import crud
from app.api import deps


router = APIRouter()

@router.get('/users', response_model=list[User])
def get_users(request: Request, db: Session = Depends(deps.get_db)) -> list[User]:
    return crud.user.get_multi(db)