from sqlalchemy import Column, Integer, DateTime, ForeignKey, String
from sqlalchemy.orm import relationship

from bot.database.connection import Engine, Base
from bot.models.users import User


class History(Base):
    __tablename__ = "history"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(User.telegram_id))
    user = relationship(User)
    num_book = Column(Integer)
    created_on = Column(DateTime)
    photo_captions = Column(String)
    photo_description = Column(String)
    history = Column(String)
    save = Column(Integer)

    def __str__(self):
        return f"{self.history}"

    def __repr__(self):
        return f"{self.history}"


if __name__ == "__main__":
    Base.metadata.create_all(bind=Engine)
