from sqlalchemy import Column, Integer, DateTime, MetaData
from sqlalchemy.orm import DeclarativeBase

from bot.database.connection import Engine


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    telegram_id = Column(Integer, unique=True)
    created_on = Column(DateTime)


if __name__ == "__main__":
    metadata = MetaData()
    Base.metadata.create_all(bind=Engine)
