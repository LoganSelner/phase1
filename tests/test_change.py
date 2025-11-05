import pytest

from coursera.change import change


def test_change():
    assert change(0) == 0
    assert change(1) == 1
    assert change(2) == 2
    assert change(3) == 3
    assert change(4) == 4
    assert change(5) == 1
    assert change(6) == 2
    assert change(7) == 3
    assert change(8) == 4
    assert change(9) == 5
    assert change(10) == 1
    assert change(11) == 2
    assert change(28) == 6
    assert change(99) == 14
    with pytest.raises(ValueError):
        change(-5)
