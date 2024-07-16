import pytest

from bot.repository.users import add_user, get_user


def test_add_user():
    add_user(123058345)
    user = get_user(123058345)
    assert user.telegram_id == 123058345


if __name__ == "__main__":
    pytest.main()
