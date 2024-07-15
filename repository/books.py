from datetime import datetime

from database.connection import SessionLocal
from models.books import Book


def get_num_book(telegram_id):
    with SessionLocal() as session:
        return (
            session.query(Book)
            .filter_by(user_id=telegram_id)
            .order_by(Book.book_num.desc())
            .first()
        )


def add_book(telegram_id, book_name):
    if get_num_book(telegram_id) is None:
        book_num = 0
    else:
        book_num = get_num_book(telegram_id).book_num

    with SessionLocal() as session:
        new_book = Book(
            user_id=telegram_id,
            data_book=datetime.now(),
            book_num=book_num + 1,
            book_name=book_name,
        )
        session.add(new_book)
        session.commit()


def get_all_book(telegram_id):
    with SessionLocal() as session:
        all_book = (
            session.query(Book)
            .filter_by(user_id=telegram_id)
            .order_by(Book.book_num.asc())
            .all()
        )

        books = ""
        for book in all_book:
            books += f"{book}\n"

        return books


def get_name_book(telegram_id, book_id):
    with SessionLocal() as session:
        return (
            session.query(Book).filter_by(user_id=telegram_id, book_num=book_id).first()
        )


def get_one_book(telegram_id, book_id, book_history):
    with open(f"books/{telegram_id}_{book_id}.docx", "w", encoding="utf-8") as file:
        for i in range(len(book_history)):
            file.write(f"Глава №{i+1}\n\n")
            file.write(str(book_history[i]))
            file.write("\n\n")
