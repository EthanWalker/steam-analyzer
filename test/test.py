from steam import (
    get_avatar,
    get_friends,
    get_games,
    get_persona,
)
import pytest

TEST_IDS = [76561197960435530,
            76561197972495328,
            76561197960434622,]


def test_packaging():
    assert True

def test_get_persona():
    tests = zip(TEST_IDS, ["Robin", "ChrisK", "al",])
    for id, persona in tests:
        assert get_persona(id) == persona

def test_persona_not_present():
    with pytest.raises(ValueError):
        result = get_persona(12345646546572145)

def test_get_avatar():
    IMAGE_EXT = ('.jpg', '.jpeg', '.png', '.gif')
    for id in TEST_IDS:
        avatar_url = get_avatar(id)
        assert avatar_url.endswith(IMAGE_EXT)

def test_avatar_not_present():
    with pytest.raises(ValueError):
        result = get_avatar(12345646546572145)

def test_get_friends():
    tests = zip(TEST_IDS, [287, 211, 160])
    for id, friends in tests:
        assert len(get_friends(id)) >= friends

def test_friends_not_present():
    with pytest.raises(ValueError):
        result = get_friends(12345646546572145)

def test_get_games():
    tests = zip(TEST_IDS, [493, 878, 595])
    for id, games in tests:
        assert get_games(id)["count"] == len(get_games(id)["games"])
        assert get_games(id)["count"] >= games

def test_games_not_present():
    with pytest.raises(ValueError):
        result = get_games(12345646546572145)