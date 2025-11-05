import pytest

from coursera.fractional_knapsack import optimal_value


def test_optimal_value():
    # Basic test case
    assert abs(optimal_value(50, [20, 30, 10], [60, 90, 20]) - 150.0) < 1e-6
    # Test with zero capacity
    assert abs(optimal_value(0, [10, 20], [60, 100]) - 0.0) < 1e-6
    # Test with no items
    assert abs(optimal_value(50, [], []) - 0.0) < 1e-6
    # Test with fractional item
    assert abs(optimal_value(10, [20], [100]) - 50.0) < 1e-6
    # Test with all items fitting
    assert abs(optimal_value(100, [10, 20, 30], [60, 100, 120]) - 280.0) < 1e-6
    # Test with negative capacity
    with pytest.raises(ValueError):
        optimal_value(-10, [10, 20], [60, 100])
    # Test with mismatched weights and values lengths
    with pytest.raises(ValueError):
        optimal_value(50, [10, 20], [60])
