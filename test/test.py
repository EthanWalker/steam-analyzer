from steam import (get_persona_name,
                   get_avatar)
import pytest

def test_packaging():
    assert True

def test_get_persona():
    tests = {76561197960435530: "Robin",
            76561197972495328: "ChrisK",
            76561197960434622: "al",}
    for id, persona in tests.items():
        assert get_persona_name(id) == persona

def test_persona_not_present():
    with pytest.raises(ValueError):
        result = get_persona_name(12345646546572145)

def test_get_avatar():
    IMAGE_EXT = ('.jpg', '.jpeg', '.png', '.gif')
    tests = {76561197960435530: "Robin",
             76561197972495328: "ChrisK",
             76561197960434622: "al",}
    for id, persona in tests.items():
        avatar_url = get_avatar(id)
        assert avatar_url.endswith(IMAGE_EXT)