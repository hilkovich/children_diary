from sqlalchemy import Column, Integer, DateTime, ForeignKey, MetaData, String
from sqlalchemy.orm import DeclarativeBase, relationship

from database.connection import Engine
from models.users import User


class Base(DeclarativeBase):
    pass


class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(User.telegram_id))
    user = relationship(User)
    data_book = Column(DateTime)
    book_num = Column(Integer)
    book_name = Column(String)


if __name__ == "__main__":
    metadata = MetaData()
    Base.metadata.create_all(bind=Engine)
