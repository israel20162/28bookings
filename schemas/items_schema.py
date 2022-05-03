from sqlalchemy import Boolean, Column, Enum, ForeignKey, String, Text, Integer, DateTime
from sqlalchemy.orm import relationship

from .mixins import TimeStamp
from .users_schema import User
from db import Base

# import enum

class Item(TimeStamp, Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    city = Column(String(255), nullable=False)
    brand = Column(String(255), default="unknown",nullable=True)
    value = Column(Integer, nullable=True)
    daily_price = Column(Integer , nullable=False)
    weekly_price = Column(Integer,default=daily_price  ,  nullable=True)
    monthly_price = Column(Integer,default=daily_price , nullable=True)
    zipcode = Column(String, nullable=False)
    rating = Column(Integer,default=1,  nullable=False)
    is_verified = Column(Boolean, default=False)
    is_available = Column(Boolean, default=True)
    quantity = Column(Integer, default=1, nullable=False)
    user = Column(Integer, ForeignKey("users.id"), nullable=False)
    item_category = Column(Integer, ForeignKey("categories.id"), nullable=False) 
    slug = Column(String(40), nullable=False)
    created_by = relationship(User, viewonly=True)
    owner = relationship("User", back_populates="items")
    item_pictures = relationship("ItemPictures", back_populates='picture')
    

    






# items = sa.Table(
#     "items",
#     metadata,
#     sa.Column("id", sa.Integer, primary_key=True),
#     sa.Column("title", sa.String(255), ),
#     sa.Column("description", sa.Text, ),
#     sa.Column("city", sa.String ),
#     sa.Column("value", sa.Integer ),
#     sa.Column("daily_price", sa.Integer, ),
#     sa.Column("user", sa.Integer, sa.ForeignKey('users.id'), ),
#     sa.Column("categories", sa.String, ),
#     sa.Column("monthly_price", sa.Integer),
#     sa.Column("weekly_price", sa.Integer),
#     sa.Column("zipcode", sa.String),
#     sa.Column("rating", sa.Integer, default=1 ),
#     sa.Column("created_at", sa.DateTime),
#     sa.Column("updated_at", sa.DateTime),
#     sa.Column("quantity", sa.Integer, default=1, ),
#     sa.Column("brand", sa.String)
# )
