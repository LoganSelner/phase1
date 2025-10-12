import pytest

from coursera.fibonacci_partial_sum import fibonacci_partial_sum


def test_fibonacci_partial_sum():
    assert fibonacci_partial_sum(3, 7) == 1
    assert fibonacci_partial_sum(10, 10) == 5
    assert fibonacci_partial_sum(10, 200) == 2
    assert fibonacci_partial_sum(0, 0) == 0
    assert fibonacci_partial_sum(1, 1) == 1
    assert fibonacci_partial_sum(0, 1) == 1
    assert fibonacci_partial_sum(1234567890, 1234567890) == 0
    with pytest.raises(ValueError):
        fibonacci_partial_sum(-1, 10)
    with pytest.raises(ValueError):
        fibonacci_partial_sum(10, -1)
    with pytest.raises(ValueError):
        fibonacci_partial_sum(10, 5)
