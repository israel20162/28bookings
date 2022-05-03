from sqlalchemy import Boolean, Column, Enum, ForeignKey, String, Text, Integer, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from db import Base

from .mixins import TimeStamp

class Rentals(TimeStamp,Base):
    __tablename__ = "rentals"

    id = Column(Integer,primary_key=True, index=True, unique=True)
    item_id = Column(Integer, ForeignKey('items.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    lendee_id = Column(Integer,ForeignKey('users.id'), nullable=False)
    cost = Column(Integer, nullable=False)
    paid = Column(Boolean, default=True)
    payment_method = Column(String(20), unique=False, nullable=False)
    rental_confirmed = Column(Boolean, default=False)
    rental_status = Column(Integer, default=False)
    duration = Column(Integer, nullable=False)
    from_date = Column(DateTime, nullable=False)
    to_date = Column(DateTime, nullable=False)
    cal_event_id = Column(String(255), nullable=True)

    

    




# import sqlalchemy as sa
# metadata = sa.MetaData()

# rentals = sa.Table(
#     "rentals",
#     metadata,
#     sa.Column("id", sa.Integer, primary_key=True),
#     sa.Column("item", sa.Integer, sa.ForeignKey('items.id')),
#     sa.Column("lendee_id", sa.Integer, sa.ForeignKey('users.id')),
#     sa.Column("lender_id", sa.Integer, sa.ForeignKey('users.id')),
#     sa.Column("booked", sa.DateTime),
#     sa.column("start_date", sa.DateTime),
#     sa.column("end_date", sa.DateTime)
# )
