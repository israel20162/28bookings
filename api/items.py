import fastapi
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException

from db import get_db
from models.item import Item, ItemCreate
from utils.items import get_item, get_items, get_items_by_category, get_items_by_user, create_item

from typing import List

router = fastapi.APIRouter()


@router.get("/api/items/", response_model=List[Item])
async def get_all_items(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    items =  get_items(db, skip=skip, limit=limit)
    return items


@router.post("/api/items/")
async def create_new_item(item: ItemCreate, db:Session = Depends(get_db)):
    return create_item(db=db, item=item)