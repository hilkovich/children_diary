from sqlalchemy import Column, Integer, DateTime, ForeignKey, MetaData, String
from sqlalchemy.orm import DeclarativeBase, relationship

from database.connection import Engine
from models.users import User


class Base(DeclarativeBase):
    pass


class History(Base):
    __tablename__ = "history"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(User.id))
    user = relationship(User)
    data_task = Column(DateTime)
    photo_caption = Column(String)
    photo_descript = Column(String)
    photo_story = Column(String)
    book_id = Column(Integer)
    story_save = Column(Integer)


if __name__ == "__main__":
    metadata = MetaData()
    Base.metadata.create_all(bind=Engine)
