
"""Tests checking implementation of Calculator class."""

import unittest
from calculator.calculator_app.calculator_app import Calculator


class TestCalculatorApp(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.add(2, 3), 5, "Results should be 5")

    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(10, 3), 7, "Results should be 7")

    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(5, 5), 25, "Results should be 25")

if __name__ == '__main__':
    unittest.main(verbosity=2)
