from pydantic import BaseModel


class Image(BaseModel):
    id: int
    url: str
    caption: str


class Tag(BaseModel):
    id_post: int | None = None
    title: str
    id: str


class PostBase(BaseModel):
    title: str | None = None
    body: str | None = None


class PostCreate(PostBase):
    pass


class Post(PostBase):
    id_post: int

    class Config:
        orm_mode = True
