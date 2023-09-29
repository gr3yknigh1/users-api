from __future__ import annotations

from pydantic import BaseModel
from pydantic.types import PositiveInt, SecretStr
from pydantic.networks import EmailStr


class UserBase(BaseModel):
    email: EmailStr


class UserCreate(UserBase):
    password: SecretStr


class User(UserBase):
    id: PositiveInt

    class Config:
        from_attributes = True


__all__ = (
    "UserBase",
    "UserCreate",
    "User",
)
