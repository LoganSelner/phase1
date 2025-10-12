from coursera.lcm import lcm


def test_lcm():
    assert lcm(4, 5) == 20
    assert lcm(0, 5) == 0
    assert lcm(4, 0) == 0
    assert lcm(0, 0) == 0
    assert lcm(-4, 5) == 20
    assert lcm(4, -5) == 20
    assert lcm(-4, -5) == 20
    assert lcm(21, 6) == 42
    assert lcm(13, 17) == 221
