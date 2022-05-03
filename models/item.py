from db import BaseModel
from datetime import datetime, timezone
from typing import Optional



class ItemBase(BaseModel):
    title: str 
    description: str
    brand:  Optional[str]
    value: int
    daily_price: int
    monthly_price: Optional[int]
    weekly_price: Optional[int] 
    item_category: int
    city: str
    zipcode: str
    rating: Optional[int]
    quantity: int
    



class Item(ItemBase):
    id: int
    created_at: datetime
    updated_at: datetime
    is_verified: bool
    is_available: bool
    user: int
    slug: str

    class Config:
        orm_mode = True
   
    
    


class ItemCreate(ItemBase):
   ...
