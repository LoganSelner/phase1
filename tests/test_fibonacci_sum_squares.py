import pytest

from coursera.fibonacci_sum_squares import fibonacci_sum_squares


def test_fibonacci_sum_squares():
    assert fibonacci_sum_squares(0) == 0
    assert fibonacci_sum_squares(1) == 1
    assert fibonacci_sum_squares(2) == 2
    assert fibonacci_sum_squares(3) == 6
    assert fibonacci_sum_squares(7) == 3
    assert fibonacci_sum_squares(10) == 5
    assert fibonacci_sum_squares(100) == 5
    assert fibonacci_sum_squares(239) == 0
    with pytest.raises(ValueError):
        fibonacci_sum_squares(-1)
