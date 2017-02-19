from steam import (
    get_avatar,
    get_friends,
    get_games,
    get_persona,
)
import pytest

def test_packaging():
    assert True

def test_get_persona():
    tests = {76561197960435530: "Robin",
            76561197972495328: "ChrisK",
            76561197960434622: "al",}
    for id, persona in tests.items():
        assert get_persona(id) == persona

def test_persona_not_present():
    with pytest.raises(ValueError):
        result = get_persona(12345646546572145)

def test_get_avatar():
    IMAGE_EXT = ('.jpg', '.jpeg', '.png', '.gif')
    tests = [76561197960435530,
             76561197972495328,
             76561197960434622,]
    for id in tests:
        avatar_url = get_avatar(id)
        assert avatar_url.endswith(IMAGE_EXT)

def test_avatar_not_present():
    with pytest.raises(ValueError):
        result = get_avatar(12345646546572145)

def test_get_friends():
    tests = [76561197960435530,
             76561197972495328,
             76561197960434622,]
    for id in tests:
        assert len(get_friends(id)) != 0

def test_friends_not_present():
    with pytest.raises(ValueError):
        result = get_friends(12345646546572145)

def test_get_games():
    tests = [76561197960435530,
             76561197972495328,
             76561197960434622,]
    for id in tests:
        assert get_games(id)["count"] == len(get_games(id)["games"])

def test_games_not_present():
    with pytest.raises(ValueError):
        result = get_games(12345646546572145)