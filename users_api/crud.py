from __future__ import annotations
from sqlalchemy.orm import Session

from . import models, schemas


def get_user(db: Session, user_id: int):
    return (
        db.query(models.UserModel)
        .filter(models.UserModel.id == user_id)
        .first()
    )


def get_user_by_email(db: Session, email: str):
    return (
        db.query(models.UserModel)
        .filter(models.UserModel.email == email)
        .first()
    )


def get_users(db: Session, *, offset=0, limit=100):
    return db.query(models.UserModel).offset(offset).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    # TODO(gr3yknigh1): Implement basic hashing
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.UserModel(email=user.email, password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
