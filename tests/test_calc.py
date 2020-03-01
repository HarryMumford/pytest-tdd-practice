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

def test_multiply_two_numbers():
    c = Calc()

    res = c.multiply(2, 2)

    assert res == 4

def test_multiply_many_numbers():
    c = Calc()

    s = range(1, 10)

    res = c.multiply(*s)

    assert res == 362880

def test_divide_two_numbers():
    c = Calc()

    res = c.divide(4, 2)

    assert res == 2

