import pytest

from bot.repository.books import get_num_book, add_book, get_name_book


def test_add_book():
    add_book(123058345, "Тестовая книга №1")
    assert get_num_book(123058345) is not None


def test_name_book():
    assert get_name_book(123058345, 1).book_name == "Тестовая книга №1"


if __name__ == "__main__":
    pytest.main()
