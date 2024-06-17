from sqlalchemy.orm import Session

from . import models, schemas


def get_post_by_id(db: Session, id_post: int):
    return db.query(models.Post).filter(models.Post.id_post == id_post).first()


def get_posts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Post).offset(skip).limit(limit).all()


def create_post(db: Session, post: schemas.PostCreate):
    db_post = models.Post(title=post.title, body=post.body)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return
