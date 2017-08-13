
"""Simple calculator class created in TDD concept."""


class Calculator(object):

    def __init__(self, x, y):
        self.x = Calculator.check_if_int_or_float(x)
        self.y = Calculator.check_if_int_or_float(y)

    @staticmethod
    def check_if_int_or_float(number):
        if not isinstance(number, (int, float)):
            raise Exception("Arguments passed to object should be of <class 'int'> or "
                            "<class 'float'>, not {0}".format(type(number)))
        else:
            return number

    def add(self):
        return self.x + self.y

    def subtract(self):
        return self.x - self.y

    def multiply(self):
        return self.x * self.y

    def divide(self):
        return self.x / self.y
