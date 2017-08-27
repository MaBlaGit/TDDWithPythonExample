
"""Simple calculator class created in TDD concept."""

import doctest


class Calculator(object):

    """Calculator class. Use docstring to check correct
    functionality of the class.

    - positive tests -

    >>> calc = Calculator(10, 10)
    >>> calc.add()
    20
    >>> calc.subtract()
    0
    >>> calc.multiply()
    100
    >>> calc.divide()
    1.0

    - negative tests -

    >>> divide_by_zero = Calculator(5, 0)
    >>> divide_by_zero.divide()
    Traceback (most recent call last):
    ...
    ValueError: You cannot divide by 0

    >>> wrong_type_one = Calculator(5, [1, 2])
    Traceback (most recent call last):
    ...
    TypeError: Arguments passed to object should be of <class 'int'> or <class 'float'>
    >>> wrong_type_two = Calculator(5, '5')
    Traceback (most recent call last):
    ...
    TypeError: Arguments passed to object should be of <class 'int'> or <class 'float'>
    >>> wrong_type_three = Calculator('10', '11')
    Traceback (most recent call last):
    ...
    TypeError: Arguments passed to object should be of <class 'int'> or <class 'float'>
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
            raise TypeError("Arguments passed to object should be of <class 'int'> or "
                            "<class 'float'>")
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
        if self.num_y == 0 or self.num_x == 0:
            raise ValueError("You cannot divide by 0")
        return self.num_x / self.num_y

if __name__ == '__main__':
    doctest.testmod()
