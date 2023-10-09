import pytest
from um import count


def test_input():
    assert count("Um, thank you.") == 1
    assert count("um") == 1
    assert count("Um, thanks, um...") == 2
    assert count("yummy") == 0
    assert count("Um?") == 1
    assert count("Um...Um... ah? um...") == 3