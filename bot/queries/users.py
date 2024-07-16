from datetime import datetime

from bot.database.connection import SessionLocal
from bot.models.users import User


def add_user(telegram_id):
    with SessionLocal() as session:
        new_user = User(
            telegram_id=telegram_id,
            created_on=datetime.now(),
        )
        session.add(new_user)
        session.commit()


def get_user(telegram_id):
    with SessionLocal() as session:
        return session.query(User).filter_by(telegram_id=telegram_id).first()
