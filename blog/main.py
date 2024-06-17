from typing import Union

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from blog import crud
from . import models, schemas
from .database import engine, get_db

##pip install psycopg2


app = FastAPI()
models.Base.metadata.create_all(bind=engine)


@app.get("/")
async def read_root():
    return {"title": "This is my blog!! Hope You enjoy it"}


@app.get("/home/")
async def read_home():
    return {"title": "This is my blog!! Hope You enjoy it"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, query: Union[str, None] = None):
    return {"item_id": item_id, "query": query}


@app.post("/posts/", response_model=schemas.Post)
async def create_post(post: schemas.PostCreate, db: Session = Depends(get_db)):
    return crud.create_post(db=db, post=post)
