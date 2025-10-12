import pytest

from coursera.fibonacci_last_digit import fibonacci_last_digit


def test_fibonacci_last_digit():
    assert fibonacci_last_digit(0) == 0
    assert fibonacci_last_digit(1) == 1
    assert fibonacci_last_digit(2) == 1
    assert fibonacci_last_digit(3) == 2
    assert fibonacci_last_digit(4) == 3
    assert fibonacci_last_digit(5) == 5
    assert fibonacci_last_digit(6) == 8
    assert fibonacci_last_digit(7) == 3
    assert fibonacci_last_digit(8) == 1
    assert fibonacci_last_digit(9) == 4
    assert fibonacci_last_digit(10) == 5
    assert fibonacci_last_digit(20) == 5
    assert fibonacci_last_digit(50) == 5
    assert fibonacci_last_digit(100) == 5
    assert fibonacci_last_digit(1000) == 5
    assert fibonacci_last_digit(10000) == 5
    assert fibonacci_last_digit(100000) == 5
    assert fibonacci_last_digit(1000000) == 5
    assert fibonacci_last_digit(10000000) == 5
    assert fibonacci_last_digit(100000000) == 5
    assert fibonacci_last_digit(1000000000) == 5
    with pytest.raises(ValueError):
        fibonacci_last_digit(-1)
