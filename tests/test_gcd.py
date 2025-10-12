from coursera.gcd import gcd


def test_gcd():
    assert gcd(48, 18) == 6
    assert gcd(101, 10) == 1
    assert gcd(56, 98) == 14
    assert gcd(0, 5) == 5
    assert gcd(5, 0) == 5
    assert gcd(0, 0) == 0
    assert gcd(-48, 18) == 6
    assert gcd(48, -18) == 6
    assert gcd(-48, -18) == 6
