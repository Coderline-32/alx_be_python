import unittest
from simple_calculator import SimpleCalculator 

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        # Set up the simple calculator instance before each test.
        self.calc = SimpleCalculator()
    
    def test_addition(self):
        self.assertEqual(self.calc.add(2,3), 5)
        self.assertEqual(self.calc.add(-2,-2), -4)
        self.assertEqual(self.calc.add(-2,2), 0)
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(2,3), -1)
        self.assertEqual(self.calc.subtract(-2,-2), 0)
        self.assertEqual(self.calc.subtract(-2,2), -4)
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(2,3), 6)
        self.assertEqual(self.calc.multiply(-2,-2), 4)
        self.assertEqual(self.calc.multiply(-2,2), -4)
    def test_division(self):
        self.assertEqual(self.calc.divide(6,2), 3)
        self.assertEqual(self.calc.divide(-2,-2), 1)
        self.assertEqual(self.calc.divide(-2,2), -1)
        self.assertIsNone(self.calc.divide(-2,0))





if __name__ == "__main__":
    unittest.main()