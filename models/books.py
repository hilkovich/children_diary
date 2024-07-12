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

    def __str__(self):
        return f"{self.book_num}. {self.book_name}"

    def __repr__(self):
        return f"{self.book_num}. {self.book_name}"


if __name__ == "__main__":
    metadata = MetaData()
    Base.metadata.create_all(bind=Engine)
