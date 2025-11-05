from coursera.largest_number import largest_number


def test_largest_number():
    assert largest_number(["21", "2"]) == "221"
    assert largest_number(["9", "4", "6", "1", "9"]) == "99641"
    assert largest_number(["23", "39", "92"]) == "923923"
    assert largest_number(["5", "50", "56"]) == "56550"
    assert largest_number(["0", "0"]) == "00"
    assert largest_number(["121", "12"]) == "12121"
    assert (
        largest_number(
            ["824", "938", "1399", "5607", "6973", "5703", "9609", "4398", "8247"]
        )
        == "9609938824824769735703560743981399"
    )
