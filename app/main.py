from fastapi import FastAPI, APIRouter, Query, HTTPException, Request, Depends
from fastapi.templating import Jinja2Templates
from typing import Optional, Any
from pathlib import Path
from sqlalchemy.orm import Session

from app.schemas.channel import Channel, ChannelCreate, ChannelSearchResults, ChannelUpdate
from app.schemas.user import User, UserCreate, UserUpdate
from app import crud
from app import deps

ROOT = Path(__file__).resolve().parent.parent

BASE_PATH = Path(__file__).resolve().parent

TEMPLATES = Jinja2Templates(directory=str(BASE_PATH / "templates"))



app = FastAPI(
    title="Hâpy API",
    description="Hâpy Checkout System Restful API.",
    version="0.1.0",
    openapi_url="/openapi.json",
    docs_url="/docs",
    debug=True,
)

api_router = APIRouter()

@api_router.get('/', status_code=200)
def root(request: Request) -> dict:
    return TEMPLATES.TemplateResponse("index.html", { "request": request })


@api_router.get('/channels', response_model=list[Channel])
def get_channels(request: Request, db: Session = Depends(deps.get_db)) -> list[Channel]:
    return crud.channel.get_multi(db)

@api_router.get('/channels/{channel_id}', response_model=Channel, status_code=200)
def get_channel(channel_id: int, request: Request, db: Session = Depends(deps.get_db)) -> Channel:
    response = crud.channel.get(db, id=channel_id)
    if not response:
        raise HTTPException(status_code=404, detail=f"Channel {channel_id} not found")
    return response

@api_router.get('/search', response_model=ChannelSearchResults, status_code=200)
def search_channels(keyword: Optional[str] = Query(None, min_length=3, example=''), max_results: Optional[int] = 10, db: Session = Depends(deps.get_db)) -> dict:
    channels = crud.channel.get_multi(db, limit=max_results)
    if not keyword:
        return {"results": channels }

    response = fiter(lambda channel: keyword.lower() in channel.name.lower(), channels)
    return {"results": list(response)[:max_results]}

@api_router.post('/channels', response_model=Channel, status_code=201)
def create_channel(channel: ChannelCreate, request: Request, db: Session = Depends(deps.get_db)) -> Channel:
    return crud.channel.create(db, obj_in=channel)


@api_router.delete('/channels/{channel_id}', status_code=204)
def delete_channel(channel_id: int, db: Session = Depends(deps.get_db)) -> None:
    response = crud.channel.get(db, id=channel_id)
    if not response:
        raise HTTPException(status_code=404, detail=f"Channel {channel_id} not found")
    return crud.channel.delete(db, channel_id=channel_id)

@api_router.put('/channels/{channel_id}', response_model=Channel, status_code=200)
def update_channel(channel_id: int, channel: ChannelUpdate, db: Session = Depends(deps.get_db)) -> Channel:
    response = crud.channel.get(db, id=channel_id)
    if not response:
        raise HTTPException(status_code=404, detail=f"Channel {channel_id} not found")
    return crud.channel.update(db, db_obj=response, obj_in=channel)


@api_router.get('/users', response_model=list[User])
def get_users(request: Request, db: Session = Depends(deps.get_db)) -> list[User]:
    return crud.user.get_multi(db)

app.include_router(api_router)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="debug")