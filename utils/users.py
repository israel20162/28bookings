from sqlalchemy.orm import Session
from models.user import UserCreate
from models.item import ItemCreate
from schemas.users_schema import User
from schemas.items_schema import Item
from utils.slug_maker import url_slugify


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()


def create_user(db: Session, user: UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = User(
        email=user.email,
        phone=user.phone, 
        password=fake_hashed_password, 
        role=user.role)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_user_item(db: Session, item: ItemCreate, user_id: int):
    created_slug = url_slugify(item.title + '-' + str(user_id))
    db_item = Item(**item.dict(), user=user_id, slug=created_slug)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


# def get_items(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.Item).offset(skip).limit(limit).all()


# def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
#     db_item = models.Item(**item.dict(), owner_id=user_id)
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item




# def get_items(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.Item).offset(skip).limit(limit).all()


# def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
#     db_item = models.Item(**item.dict(), owner_id=user_id)
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item
