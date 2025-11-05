import pytest

from coursera.car_fueling import min_refills


def test_min_refills():
    # Basic test cases
    assert min_refills(950, 400, [200, 375, 550, 750]) == 2
    assert min_refills(10, 3, [1, 2, 5, 9]) == -1
    assert min_refills(200, 250, []) == 0

    # Edge cases
    assert min_refills(0, 100, []) == 0  # No distance to travel
    assert min_refills(100, 100, []) == 0  # Exact tank capacity
    assert min_refills(100, 50, [25, 50, 75]) == 1  # Multiple stops but only one needed

    # Cases with stops at the beginning and end
    assert min_refills(300, 100, [0, 100, 200, 300]) == 2
    assert min_refills(300, 150, [0, 150, 300]) == 1

    # Cases with unreachable stops
    assert min_refills(500, 100, [150, 300, 450]) == -1
    assert min_refills(600, 200, [250, 450]) == -1
    assert min_refills(700, 200, [100, 200, 300, 400]) == -1

    # Large input case
    stops = list(range(100, 10000, 100))
    assert min_refills(10000, 300, stops) == 33

    # Invalid input cases
    with pytest.raises(ValueError):
        min_refills(-100, 100, [50, 75])
    with pytest.raises(ValueError):
        min_refills(100, -50, [25, 50])
    with pytest.raises(ValueError):
        min_refills(100, 50, [-10, 20, 30])
