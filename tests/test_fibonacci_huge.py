import pytest

from coursera.fibonacci_huge import fibonacci_huge, get_pisano_period


def test_get_pisano_period():
    assert get_pisano_period(2) == 3
    assert get_pisano_period(3) == 8
    assert get_pisano_period(4) == 6
    assert get_pisano_period(5) == 20
    assert get_pisano_period(6) == 24
    with pytest.raises(ValueError):
        get_pisano_period(0)
    with pytest.raises(ValueError):
        get_pisano_period(-5)


def test_fibonacci_huge():
    assert fibonacci_huge(0, 10) == 0
    assert fibonacci_huge(1, 10) == 1
    assert fibonacci_huge(10, 2) == 1
    assert fibonacci_huge(2015, 3) == 1
    assert fibonacci_huge(239, 1000) == 161
    assert fibonacci_huge(2816213588, 239) == 151
    assert fibonacci_huge(9999999999999, 2) == 0
    with pytest.raises(ValueError):
        fibonacci_huge(-1, 10)
    with pytest.raises(ValueError):
        fibonacci_huge(10, 0)
    with pytest.raises(ValueError):
        fibonacci_huge(10, -5)
