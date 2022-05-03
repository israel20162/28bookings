from pydantic import BaseModel
from datetime import datetime, timezone
from .item import Item


class UserBase(BaseModel):
    email: str
    phone: str
    password: str
    role: int



class User(UserBase):
    id: int 
    is_active: bool
    is_verified: bool
    created_at: datetime
    updated_at: datetime
    items: list[Item] = []

    class Config:
        orm_mode = True;
    


class UserCreate(UserBase):
    ...

   