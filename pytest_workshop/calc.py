from functools import reduce

class Calc:
    def add(self, *s):
        return sum(s)

    def subtract(self, a, b):
        return a - b

    def multiply(self, *s):
        return reduce(lambda x, y: x * y, s)
    
    def divide(self, a, b):
        return a // b
    
