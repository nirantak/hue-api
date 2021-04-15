from hue import api


def test_initial_state():
    assert api.ORIGINAL_STATE == {}
    assert "/api/" in api.HUE_API
