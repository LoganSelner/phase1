import pytest

from coursera.different_summands import optimal_summands


def test_optimal_summands():
    # Basic test cases
    assert optimal_summands(6) == [1, 2, 3]
    assert optimal_summands(8) == [1, 2, 5]
    assert optimal_summands(2) == [2]
    assert optimal_summands(7) == [1, 2, 4]

    # Edge cases
    assert optimal_summands(1) == [1]
    assert optimal_summands(3) == [1, 2]

    # Larger numbers
    assert optimal_summands(15) == [1, 2, 3, 4, 5]
    assert optimal_summands(20) == [1, 2, 3, 4, 10]

    # Invalid input
    with pytest.raises(ValueError):
        optimal_summands(0)
    with pytest.raises(ValueError):
        optimal_summands(-5)
