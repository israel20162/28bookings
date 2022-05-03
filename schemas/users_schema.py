from sqlalchemy import Boolean, Column, Enum, ForeignKey, String, Text, Integer, DateTime
from sqlalchemy.orm import relationship
import enum
from db import Base

from .mixins import TimeStamp

class Role(enum.IntEnum):
    admin = 1
    staff = 2
    user = 3
    

class User(TimeStamp, Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)  
    email = Column(String(255), nullable=False, unique=True)
    is_verified = Column(Boolean, default=False)
    phone = Column(String(255), nullable=False, unique=True)
    role = Column(Enum(Role), default='3')
    password = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True)

    profile = relationship("Profile", back_populates="owner", uselist=False)
    items = relationship("Item", back_populates="owner")



class Profile(Base):
    __tablename__ = "profiles"

    id = Column(Integer,primary_key=True, index=True)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    bio = Column(Text, nullable=True)
    
    rated = Column(Boolean, default=False)
    rating = Column(Integer, default=1)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    owner = relationship("User", back_populates="profile")





# users = sa.Table(
#     "users",
#     metadata,
#     sa.Column("id", sa.Integer, primary_key=True),
#     sa.Column('first_name', sa.String),
#     sa.Column('last_name', sa.String),
#     sa.Column("email", sa.String)
# )
