from datetime import datetime

from database.connection import SessionLocal
from models.history import History


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
