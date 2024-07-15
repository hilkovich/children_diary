import pytest

from repository.prediction import gen_story, gen_message


def test_gen_story():
    message = "Напиши историю про Колю на 50 слов"
    story = gen_story(message)
    assert isinstance(story, str)


def test_gen_message():
    captions = ["Описание мальчика", "Описание девочки"]
    descript = "Тестовое примечание"
    message = gen_message(captions, descript)
    assert "Описание мальчика" in message
    assert "Описание девочки" in message
    assert "Тестовое примечание" in message


if __name__ == "__main__":
    pytest.main()
