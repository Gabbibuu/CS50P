from bank import value


def test_greeting():
    assert value("hello") == 0
    assert value("HELLO") == 0
    assert value("hi") == 20
    assert value("HI") == 20
    assert value("wassup") == 100
    assert value("WASSUP") == 100