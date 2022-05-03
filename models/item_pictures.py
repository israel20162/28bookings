from pydantic import BaseModel
from datetime import datetime, timezone
from typing import Optional


class ItemPictureBase(BaseModel):
    url: str
    item_id: int



class ItemPicture(ItemPictureBase):
    id: int 
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True;
    


class ItemPictureCreate(ItemPictureBase):
    ...

   