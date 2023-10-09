import pytest
from working import convert


def test_convert():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("5 PM to 9 AM") == "17:00 to 09:00"
    assert convert("5:30 PM to 9:50 AM") == "17:30 to 09:50"

def test_value_error():
    with pytest.raises(ValueError):
        convert("9AM - 5PM")
    with pytest.raises(ValueError):
        convert("09:00 to 17:00")
    with pytest.raises(ValueError):
        convert("15:00 AM to 25:00 PM")
    with pytest.raises(ValueError):
        convert("1:60 AM to 1:60 PM")