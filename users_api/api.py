from __future__ import annotations
from typing import Sequence

from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
import fastapi

from . import crud, models, schemas
from .db import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)

api_router = fastapi.APIRouter(prefix="/api/v1")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@api_router.post("/users", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user is not None:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@api_router.get("/users", response_model=Sequence[schemas.User])
def get_users(
    offset: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    users = crud.get_users(db, offset=offset, limit=limit)
    return users


@api_router.get("/users/{user_id}", response_model=schemas.User)
def get_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@api_router.get("/health")
def check_health():
    return "OK"
