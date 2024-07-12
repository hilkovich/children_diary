from datetime import datetime

from database.connection import SessionLocal
from models.books import Book


def get_num_book(telegram_id):
    with SessionLocal() as session:
        num = (
            session.query(Book)
            .filter_by(user_id=telegram_id)
            .order_by(Book.book_num.desc())
            .first()
        )
        return num.book_num


def add_book(telegram_id, book_name):
    if get_num_book(telegram_id) is None:
        book_num = 1
    else:
        book_num = get_num_book(telegram_id)

    with SessionLocal() as session:
        new_book = Book(
            user_id=telegram_id,
            data_book=datetime.now(),
            book_num=book_num + 1,
            book_name=book_name,
        )
        session.add(new_book)
        session.commit()
