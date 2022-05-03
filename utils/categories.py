from sqlalchemy.orm import Session
from models.category import CategoryCreate
from schemas.categories_schema import Categories
from .slug_maker import url_slugify


def get_Category(db: Session, cat_id: int):
    return db.query(Categories).filter(Categories.id == cat_id).first()


def get_categories_by_parent(db: Session, parent_id: int):
    return db.query(Categories).filter(Categories.parent  == parent_id)


def get_categories(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Categories).offset(skip).limit(limit).all()


def create_category(db: Session, category: CategoryCreate):
    created_slug = url_slugify(category.name)
    db_category = Categories(
        parent=category.parent,
        name=category.name,
        description=category.description,
        image=category.image,
        slug=created_slug)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category


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
