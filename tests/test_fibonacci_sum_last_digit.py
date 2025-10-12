import pytest

from coursera.fibonacci_sum_last_digit import fibonacci_sum


def test_fibonacci_sum():
    assert fibonacci_sum(0) == 0
    assert fibonacci_sum(1) == 1
    assert fibonacci_sum(3) == 4
    assert fibonacci_sum(7) == 3
    assert fibonacci_sum(10) == 3
    assert fibonacci_sum(100) == 5
    assert fibonacci_sum(1000) == 5
    assert fibonacci_sum(10000) == 5
    assert fibonacci_sum(100000) == 5
    assert fibonacci_sum(1000000) == 5
    assert fibonacci_sum(10000000) == 5
    assert fibonacci_sum(100000000) == 5
    assert fibonacci_sum(1000000000) == 5
    with pytest.raises(ValueError):
        fibonacci_sum(-1)
