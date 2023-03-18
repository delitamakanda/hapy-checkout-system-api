from pydantic import BaseModel, HttpUrl
from typing import Sequence

# TODO

class ChannelBase(BaseModel):
    pass

class ChannelCreate(ChannelBase):
    pass

class ChannelUpdate(ChannelBase):
    pass

class ChannelInDBBase(ChannelBase):
    id: int
    submitter_id: int

    class Config:
        orm_mode = True

class Channel(ChannelInDBBase):
    pass

class ChannelInDB(ChannelInDBBase):
    pass

class ChannelSearchResults(BaseModel):
    results: Sequence[Channel]

