from datetime import datetime

from bot.database.connection import SessionLocal
from bot.models.history import History


def add_history(
    telegram_id, photo_caption, photo_descript, photo_story, book_id=None, story_save=0
):
    with SessionLocal() as session:
        new_history = History(
            user_id=telegram_id,
            book_id=book_id,
            data_task=datetime.now(),
            photo_caption=photo_caption,
            photo_descript=photo_descript,
            photo_story=photo_story,
            story_save=story_save,
        )
        session.add(new_history)
        session.commit()


def get_all_history(telegram_id, book_id):
    with SessionLocal() as session:
        all_history = (
            session.query(History)
            .filter_by(user_id=telegram_id, book_id=book_id, story_save=1)
            .order_by(History.data_task.asc())
            .all()
        )

        return all_history
