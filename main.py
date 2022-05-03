import os

import sqlalchemy

from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware
from db import database
from db import Base

from api import users, items, categories, item_pictures

from db import engine

from schemas import item_pictures_schema, items_schema, users_schema, rentals_schema, categories_schema

items_schema.Base.metadata.create_all(bind=engine)
item_pictures_schema.Base.metadata.create_all(bind=engine)
users_schema.Base.metadata.create_all(bind=engine)
categories_schema.Base.metadata.create_all(bind=engine)
rentals_schema.Base.metadata.create_all(bind=engine)


app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get("/")
def read_root():
    return {"Hello": "World"}


app.include_router(users.router)
app.include_router(items.router)
app.include_router(categories.router)
app.include_router(item_pictures.router)



