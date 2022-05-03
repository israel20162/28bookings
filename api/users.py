import fastapi
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException

from db import get_db
from models.user import User, UserCreate
from models.item import Item, ItemCreate
from utils.users import get_users, get_user, create_user, create_user_item

from typing import List

router = fastapi.APIRouter()


@router.get("/api/users/", response_model=List[User])
async def get_all_users(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    users =  get_users(db, skip=skip, limit=limit)
    return users


@router.post("/api/users/")
async def create_new_user(user: UserCreate, db:Session = Depends(get_db)):
    return create_user(db=db, user=user)


@router.post("/api/users/{user_id}/items/", response_model=Item)
def create_item_for_user(
    user_id: int, item: ItemCreate, db: Session = Depends(get_db)
):
    return create_user_item(db=db, item=item, user_id=user_id)