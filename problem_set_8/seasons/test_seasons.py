from seasons import convert


def test_date():
    assert convert(8599) == "Twelve million, three hundred eighty-two thousand, five hundred sixty minutes"
    assert convert(365) == "Five hundred twenty-five thousand, six hundred minutes"
