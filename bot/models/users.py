from sqlalchemy import Column, Integer, DateTime

from bot.database.connection import Engine, Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    telegram_id = Column(Integer, unique=True)
    created_on = Column(DateTime)


if __name__ == "__main__":
    Base.metadata.create_all(bind=Engine)
