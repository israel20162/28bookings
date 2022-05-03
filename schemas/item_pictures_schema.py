from sqlalchemy import Boolean, Column, Enum, ForeignKey, String, Text, Integer, DateTime
from sqlalchemy.orm import relationship
from schemas.items_schema import Item

from .mixins import TimeStamp
from db import Base

class ItemPictures(TimeStamp, Base):
    __tablename__ = 'item_pictures'

    id = Column(Integer,primary_key=True, index=True)
    url = Column(String)
    item_id = Column(Integer, ForeignKey('items.id'), nullable=False)

    picture = relationship(Item, back_populates="item_pictures")

