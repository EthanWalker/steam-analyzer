from steam import get_persona_name
import pytest

def test_packaging():
    assert True

def test_persona():
    result = get_persona_name(76561197960435530)
    answer = "Robin"
    assert result == answer

def test_persona_not_present():
    with pytest.raises(IndexError):
        result = get_persona_name(12345646546572145)