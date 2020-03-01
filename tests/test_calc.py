from pytest_workshop.calc import Calc

def test_add_two_numbers(): 
    c = Calc()

    res = c.add(4, 5)

    assert res == 9

def test_add_many_numners():
    c = Calc()

    s = range(100)

    res = c.add(*s)

    assert res == 4950

def test_subtract_two_numners():
    c = Calc()

    res = c.subtract(2, 1)

    assert res == 1

