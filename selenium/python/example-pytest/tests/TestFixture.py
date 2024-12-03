import pytest

def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

@pytest.mark.parametrize("a, b, expected", [
    (5, 5, 10),
    (20, 2, 22),
    (12, 8, 20)
])
def test_plus(a, b, expected):
    actual = plus(a, b)
    assert expected == actual