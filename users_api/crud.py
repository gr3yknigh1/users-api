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
    fake_hashed_password = user.password.get_secret_value() + "notreallyhashed"
    db_user = models.UserModel(email=user.email, password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(db: Session, user: models.UserModel):
    # TODO(gr3yknigh1): Find the way to pass user_id directry in order to
    # bypass query duplication
    db_user = db.query(models.UserModel).get(user.id)
    db.delete(db_user)
    db.commit()
    return


def update_user(
    db: Session, updated_user: schemas.UserCreate, user: models.UserModel
):
    # TODO(gr3yknigh1): Find the way to pass user_id directry in order to
    # bypass query duplication
    db_user = (
        db.query(models.UserModel)
        .filter(models.UserModel.id == user.id)
        .update(
            {
                "email": updated_user.email,
                "password": updated_user.password,
            }
        )
    )
    db.commit()
    return db_user


__all__ = (
    "get_user",
    "get_user_by_email",
    "get_users",
    "create_user",
    "delete_user",
    "update_user",
)
