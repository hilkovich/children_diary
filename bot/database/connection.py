import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from bot.models.users import Base as UserBase
from bot.models import Base as BookBase
from bot.models.history import Base as HistoryBase

load_dotenv()

username = os.getenv("POSTGRES_USER")
password = os.getenv("POSTGRES_PASSWORD")
host = os.getenv("POSTGRES_HOST")
port = os.getenv("POSTGRES_PORT")
database = os.getenv("POSTGRES_DATABASE")

Engine = create_engine(f"postgresql://{username}:{password}@{host}:{port}/{database}")

SessionLocal = sessionmaker(bind=Engine)

Base = declarative_base()

UserBase.metadata.create_all(bind=Engine)
BookBase.metadata.create_all(bind=Engine)
HistoryBase.metadata.create_all(bind=Engine)
