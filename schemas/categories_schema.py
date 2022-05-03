from sqlalchemy import Boolean, Column, Enum, ForeignKey, String, Text, Integer, DateTime
from sqlalchemy.orm import relationship


from .mixins import TimeStamp
from db import Base

class Categories(TimeStamp, Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, unique=True)
    description = Column(String)
    image = Column(String, nullable=False)
    parent = Column(Integer, ForeignKey("categories.id"))
    slug = Column(String(100), nullable=False)

  


# categories = sa.Table(
#     "categories",
#     metadata,
#     sa.Column("id", sa.Integer, primary_key=True),
#     sa.Column("name", sa.String, ),
#     sa.Column("description", sa.String, ),
#     sa.Column("image", sa.String),
# )
