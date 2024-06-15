from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel, Field

class Image(BaseModel):
    id: int
    url: str
    caption: str

class Tag(BaseModel):
    id: int
    title: str

class PostBase(BaseModel):
    title: str
    body: Optional[str] = None

class PostCreate(PostBase):
    pass

class Post(PostBase):
    id_post: int
    class Config:
        orm_mode = True