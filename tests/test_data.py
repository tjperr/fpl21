from fpl21.data import get_position

def test_get_position():
    assert get_position(1) == 1
    assert get_position(5) == 2
    assert get_position(3) == 3
    assert get_position(4) == 4
