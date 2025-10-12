import pytest

from coursera.max_pairwise_product import max_pairwise_product


def test_max_pairwise_product():
    assert max_pairwise_product([1, 2, 3]) == 6
    assert max_pairwise_product([-1, -2, -3]) == 6
    assert max_pairwise_product([0, 0, 0]) == 0
    assert max_pairwise_product([1.5, 2.5, 3.5]) == 8.75
    assert max_pairwise_product([-1.5, -2.5, -3.5]) == 8.75
    assert max_pairwise_product([1, -2, 3]) == 3
    with pytest.raises(ValueError):
        max_pairwise_product([1])
    with pytest.raises(ValueError):
        max_pairwise_product([])
