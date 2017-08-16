
"""Simple calculator class created in TDD concept."""

import doctest

class Calculator(object):

    """Calculator class. Use docstring to check correct
    functionality of the class.
    >>> calc = Calculator(10, 10)
    >>> calc.add()
    20
    >>> calc.multiply()
    100
    """

    def __init__(self, num_x, num_y):
        self.num_x = Calculator.check_if_int_or_float(num_x)
        self.num_y = Calculator.check_if_int_or_float(num_y)

    @staticmethod
    def check_if_int_or_float(number):
        """Static method which checks type of parameters.
        :param number (int)
        :return number(int)"""

        if not isinstance(number, (int, float)):
            raise Exception("Arguments passed to object should be of <class 'int'> or "
                            "<class 'float'>, not {0}".format(type(number)))
        else:
            return number

    def add(self):
        """Add parameters."""
        return self.num_x + self.num_y

    def subtract(self):
        """Subtract parameters."""
        return self.num_x - self.num_y

    def multiply(self):
        """Multiply parameters."""
        return self.num_x * self.num_y

    def divide(self):
        """Divide parameters."""
        return self.num_x / self.num_y

if __name__ == '__main__':
    doctest.testmod()
