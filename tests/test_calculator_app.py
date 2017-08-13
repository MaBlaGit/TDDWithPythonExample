
"""Tests checking implementation of Calculator class."""

import unittest
from calculator.calculator_app.calculator_app import Calculator


class TestCalculatorApp(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator(2, 5)

    def test_add(self):
        self.assertEqual(self.calculator.add(), 7, "Results should be 7")

    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(), -3, "Results should be -3")

    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(), 10, "Results should be 10")

if __name__ == '__main__':
    unittest.main(verbosity=2)
