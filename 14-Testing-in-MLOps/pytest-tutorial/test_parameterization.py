#Run same test with multiple inputs

import pytest


@pytest.mark.parametrize("a,b,expected", [
    (1,2,3),
    (-1,1,0),
    (0,0,0),
    (10,20,30),
    (-10,10,0),
    (10,20,30)
])

def test_add(a,b,expected):
    assert a+b == expected

