from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from .config import read_env

config = read_env()

# f"postgresql+psycopg2://
SQLALCHEMY_DATABASE_URL = (
    "postgresql+psycopg2://{user}:{password}@{addr}:{port}/{db}".format(
        user=config["POSTGRES_USER"],
        password=config["POSTGRES_PASSWORD"],
        addr=config["POSTGRES_ADDR"],
        port=config["POSTGRES_PORT"],
        db=config["POSTGRES_DB"],
    )
)
print(SQLALCHEMY_DATABASE_URL)

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


__all__ = (
    "engine",
    "SessionLocal",
    "Base",
)
