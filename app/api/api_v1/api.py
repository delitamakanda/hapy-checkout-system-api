from fastapi import APIRouter

from app.api.api_v1.endpoints import channel
from app.api.api_v1.endpoints import user
from app.api.api_v1.endpoints import auth


api_router = APIRouter()
api_router.include_router(channel.router, prefix="/channels", tags=["channels"])
api_router.include_router(user.router, prefix="/users", tags=["users"])
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
