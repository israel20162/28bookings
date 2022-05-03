from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from pydantic import BaseModel
from dotenv import load_dotenv
import databases


load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

database = databases.Database(DATABASE_URL)

engine = create_engine(
    DATABASE_URL, connect_args={}, future=True
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, future=True
                            )

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
