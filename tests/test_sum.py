# Tests for sum_of_digits function
from coursera.sum_digits import sum_of_digits


def test_sum_of_digits():
    assert sum_of_digits(123, 456) == 579
    assert sum_of_digits(0, 0) == 0
    assert sum_of_digits(-1, 1) == 0
    assert sum_of_digits(999, 1) == 1000
    assert sum_of_digits(-50, -50) == -100
