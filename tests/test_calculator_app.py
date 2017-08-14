
"""Tests checking implementation of Calculator class."""

import unittest
from calculator_app.calculator_app import Calculator


class TestCalculatorApp(unittest.TestCase):
    """Calculator test class."""

    def setUp(self):
        """Set up tests."""
        self.calculator = Calculator(2, 5)

    def test_add(self):
        """Test addition."""
        self.assertEqual(self.calculator.add(), 7, "Results should be 7")

    def test_subtract(self):
        """Test subtraction."""
        self.assertEqual(self.calculator.subtract(), -3, "Results should be -3")

    def test_multiply(self):
        """Test multiplication."""
        self.assertEqual(self.calculator.multiply(), 10, "Results should be 10")

    def test_divide(self):
        """Test division."""
        self.assertEqual(self.calculator.divide(), 0.4, "Results should be 0.4")

if __name__ == '__main__':
    unittest.main(verbosity=2)
