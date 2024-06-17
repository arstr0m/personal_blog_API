from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship

from .database import Base

##pip install sqlalchemy


post_tags = Table("post_tags", Base.metadata,
                  Column("post_id", Integer, ForeignKey("posts.id_post"), primary_key=True),
                  Column("tag_id", Integer, ForeignKey("tags.id_tag"), primary_key=True)
                  )
post_images = Table("post_images", Base.metadata,
                    Column("post_id", Integer, ForeignKey("posts.id_post"), primary_key=True),
                    Column("image_id", Integer, ForeignKey("images.id_image"), primary_key=True)
                    )


class Post(Base):
    __tablename__ = "posts"

    id_post = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    body = Column(String, index=True)


'''
class Post(Base):
    __tablename__ = "posts"
    id_post = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    body = Column(String, index=True)

    tags = relationship("tags", secondary=post_tags, back_populates="posts")
    images = relationship("images", secondary=post_images, back_populates="posts")

'''


class Images(Base):
    __tablename__ = "images"
    id_image = Column(Integer, primary_key=True)
    added_at = Column(DateTime, default=datetime.now())
    url = Column(String)
    caption = Column(String)
    posts = relationship("post", secondary=post_images, back_populates="images")


class Tags(Base):
    __tablename__ = "tags"
    id_tag = Column(Integer, primary_key=True)
    title = Column(String, unique=True, index=True)
    status = Column(String(3), default="ACT")
    posts = relationship("post", secondary=post_tags, back_populates="tags")
