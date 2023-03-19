from fastapi import FastAPI, APIRouter, Query, HTTPException, Request, Depends
from typing import Optional, Any
from sqlalchemy.orm import Session

from app.schemas.channel import Channel, ChannelCreate, ChannelSearchResults, ChannelUpdate
from app import crud
from app.api import deps

router = APIRouter()


@router.get('/channels', response_model=list[Channel])
def get_channels(request: Request, db: Session = Depends(deps.get_db)) -> list[Channel]:
    return crud.channel.get_multi(db)

@router.get('/channels/{channel_id}', response_model=Channel, status_code=200)
def get_channel(channel_id: int, request: Request, db: Session = Depends(deps.get_db)) -> Channel:
    response = crud.channel.get(db, id=channel_id)
    if not response:
        raise HTTPException(status_code=404, detail=f"Channel {channel_id} not found")
    return response

@router.get('/search', response_model=ChannelSearchResults, status_code=200)
def search_channels(keyword: Optional[str] = Query(None, min_length=3, example=''), max_results: Optional[int] = 10, db: Session = Depends(deps.get_db)) -> dict:
    channels = crud.channel.get_multi(db, limit=max_results)
    if not keyword:
        return {"results": channels }

    response = filter(lambda channel: keyword.lower() in channel.name.lower(), channels)
    return {"results": list(response)[:max_results]}

@router.post('/channels', response_model=Channel, status_code=201)
def create_channel(channel: ChannelCreate, request: Request, db: Session = Depends(deps.get_db)) -> Channel:
    return crud.channel.create(db, obj_in=channel)


@router.delete('/channels/{channel_id}', status_code=204)
def delete_channel(channel_id: int, db: Session = Depends(deps.get_db)) -> None:
    response = crud.channel.get(db, id=channel_id)
    if not response:
        raise HTTPException(status_code=404, detail=f"Channel {channel_id} not found")
    return crud.channel.delete(db, channel_id=channel_id)

@router.put('/channels/{channel_id}', response_model=Channel, status_code=200)
def update_channel(channel_id: int, channel: ChannelUpdate, db: Session = Depends(deps.get_db)) -> Channel:
    response = crud.channel.get(db, id=channel_id)
    if not response:
        raise HTTPException(status_code=404, detail=f"Channel {channel_id} not found")
    return crud.channel.update(db, db_obj=response, obj_in=channel)

