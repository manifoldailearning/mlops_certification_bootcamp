def add(a,b):
    return a+b

def test_add():
    assert add(1,2) == 3
    assert add(-1,1) == 0
    assert add(0,0) == 0
    assert add(10,20) == 30
    assert add(-10,10) == 0
    assert add(10,20) == 30

