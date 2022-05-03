from sqlalchemy.orm import Session
from models.item_pictures import ItemPictureCreate
from schemas.item_pictures_schema import ItemPictures


def get_picture(db: Session, picture_id: int):
    return db.query(ItemPictures).filter(ItemPictures.id == picture_id).first()

def get_pictures_by_item(db: Session, item_id : int):
    return db.query(ItemPictures).filter(ItemPictures.item_id == item_id).all()



def create_item_picture(db: Session, picture: ItemPictureCreate):
    db_item_picture = ItemPictures(
        url = picture.url,
        item_id = picture.item_id
        )
    db.add(db_item_picture)
    db.commit()
    db.refresh(db_item_picture)
    return db_item_picture



