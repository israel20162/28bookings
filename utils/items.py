from sqlalchemy.orm import Session
from models.item import ItemCreate
from schemas.items_schema import Item


def get_item(db: Session, item_id: int):
    return db.query(Item).filter(Item.id == item_id).first()


def get_items_by_category(db: Session, cat_id : int):
    return db.query(Item).filter(Item.item_category == cat_id).all()

def get_items_by_user(db: Session, user_id : int):
    return db.query(Item).filter(Item.user == user_id).all()


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Item).offset(skip).limit(limit).all()


def create_item(db: Session, item: ItemCreate):
    db_item = Item(
        title= item.title,
        description= item.description,
        brand= item.brand,
        value= item.value,
        daily_price= item.daily_price,
        weekly_price= item.weekly_price,
        monthly_price= item.monthly_price,
        user= item.user,
        item_category = item.item_category,
        city= item.city,
        zipcode= item.zipcode,
        quantity= item.quantity
        )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


