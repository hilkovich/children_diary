import pytest

from bot.repository.history import add_history, get_all_history


def test_add_history():
    telegram_id = 123058345
    photo_caption = "Тестовое описание фотографий"
    photo_descript = "Тестовое примечание"
    photo_story = "Тестовая история"
    book_id = 12
    add_history(telegram_id, photo_caption, photo_descript, photo_story, book_id, 1)
    all_history = get_all_history(telegram_id, book_id)
    assert len(all_history) == 1


if __name__ == "__main__":
    pytest.main()
