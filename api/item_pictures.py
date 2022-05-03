import fastapi
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException

from db import get_db
from models.item_pictures import ItemPicture, ItemPictureCreate
from utils.item_pictures import get_pictures_by_item, create_item_picture, get_picture

from typing import List

router = fastapi.APIRouter()




@router.get("/api/item/picture/{picture_id}", response_model=ItemPicture)
async def get_picture_for_item(picture_id: int, db: Session = Depends(get_db)):
    picture =  get_picture(db = db, picture_id=picture_id)
    if picture is None:
        raise HTTPException(status_code=404, detail="Pictures not found")
    return picture

@router.get("/api/item/pictures/{item_id}", response_model=list[ItemPicture])
async def get_pictures_for_items(item_id: int, db: Session = Depends(get_db)):
    pictures =  get_pictures_by_item(db = db, item_id=item_id)
    if pictures is None:
        raise HTTPException(status_code=404, detail="Pictures not found")
    return pictures



@router.post("/api/items/pictures")
async def create_new_item_picture(picture: ItemPictureCreate, db:Session = Depends(get_db)):
    return create_item_picture(db=db, picture=picture)