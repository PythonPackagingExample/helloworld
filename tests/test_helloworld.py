from helloworld import get_helloworld

def test_get_helloworld():
    _helloworld = get_helloworld()
    assert "hello" in _helloworld
