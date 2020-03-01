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

