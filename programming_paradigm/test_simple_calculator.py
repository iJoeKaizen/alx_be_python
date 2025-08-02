import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Initialize a SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test addition operation."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(-5, -7), -12)

    def test_subtraction(self):
        """Test subtraction operation."""
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(0, 0), 0)
        self.assertEqual(self.calc.subtract(-3, -6), 3)
        self.assertEqual(self.calc.subtract(3, 5), -2)

    def test_multiplication(self):
        """Test multiplication operation."""
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(0, 5), 0)
        self.assertEqual(self.calc.multiply(-4, -3), 12)

    def test_division(self):
        """Test division operation."""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(-9, 3), -3)
        self.assertEqual(self.calc.divide(0, 5), 0)
        self.assertEqual(self.calc.divide(5, 2), 2.5)

    def test_division_by_zero(self):
        """Test division by zero returns None."""
        self.assertIsNone(self.calc.divide(5, 0))
        self.assertIsNone(self.calc.divide(0, 0))
        self.assertIsNone(self.calc.divide(-10, 0))

if __name__ == "__main__":
    unittest.main()
