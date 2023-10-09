from twttr import shorten


def test_assert():
    assert shorten("aeiou") == ""
    assert shorten("AEIOU") == ""
    assert shorten("twitter") == "twttr"
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("tW1TT3r") == "tW1TT3r"
    assert shorten("aeiouAEIOU.0O") == ".0"
