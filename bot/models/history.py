from sqlalchemy import Column, Integer, DateTime, ForeignKey, MetaData, String
from sqlalchemy.orm import DeclarativeBase, relationship

from bot.database.connection import Engine
from bot.models.users import User


class Base(DeclarativeBase):
    pass


class History(Base):
    __tablename__ = "history"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(User.telegram_id))
    user = relationship(User)
    book_id = Column(Integer)
    data_task = Column(DateTime)
    photo_caption = Column(String)
    photo_descript = Column(String)
    photo_story = Column(String)
    story_save = Column(Integer)

    def __str__(self):
        return f"{self.photo_story}"

    def __repr__(self):
        return f"{self.photo_story}"


if __name__ == "__main__":
    metadata = MetaData()
    Base.metadata.create_all(bind=Engine)
