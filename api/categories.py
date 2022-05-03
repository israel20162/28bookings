import fastapi
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException

from db import get_db
from models.category import Category, CategoryCreate
from utils.categories import get_categories, get_categories_by_parent, get_Category, create_category

from typing import List

router = fastapi.APIRouter()


@router.get("/api/categories/", response_model=List[Category])
async def get_all_categories(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    categories =  get_categories(db, skip=skip, limit=limit)
    return categories


@router.post("/api/categories/")
async def create_new_category(category: CategoryCreate, db:Session = Depends(get_db)):
    return create_category(db=db, category=category)