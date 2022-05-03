from pydantic import BaseModel
from datetime import datetime, timezone
from typing import Optional


class CategoryBase(BaseModel):
    name : str
    description : str
    image : str
    parent : Optional[int]



class Category(CategoryBase):
    id: int 
    created_at: datetime
    updated_at: datetime
    

    class Config:
        orm_mode = True;
    


class CategoryCreate(CategoryBase):
    ...

   