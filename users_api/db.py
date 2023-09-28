from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from .config import read_env

config = read_env()

SQLALCHEMY_DATABASE_URL = "postgresql://{user}:{password}@{addr}/{db}".format(
    user=config["POSTGRES_USER"],
    password=config["POSTGRES_PASSWORD"],
    addr=config["POSTGRES_ADDR"],
    db=config["POSTGRES_DB"],
)

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
