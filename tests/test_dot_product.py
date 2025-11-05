import pytest

from coursera.dot_product import max_dot_product


def test_max_dot_product():
    assert max_dot_product([1, 3, -5], [-2, 4, 1]) == 23
    assert max_dot_product([0, 1, 2], [2, 1, 0]) == 5
    assert max_dot_product([1, 2, 3], [4, 5, 6]) == 32
    assert max_dot_product([-1, -2, -3], [-4, -5, -6]) == 32
    assert max_dot_product([1], [1]) == 1
    assert max_dot_product([], []) == 0
    with pytest.raises(ValueError):
        max_dot_product([1, 2], [1])
