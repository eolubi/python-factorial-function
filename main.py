import unittest
# import the py file where the factorial function was written
from factorial import factorial


class TestFactorial(unittest.TestCase):
    """
    A test case class that inherits from the unittest.TestCase class.
    It contains individual test methods to test different scenarios for the factorial function.
    """

    def test_factorial_zero(self):
        """
        Test whether the factorial of 0 is 1.
        """
        self.assertEqual(factorial(0), 1)

    def test_factorial_positive(self):
        """
        Test whether the factorial of a positive integer is calculated correctly.
        """
        self.assertEqual(factorial(5), 120)

    def test_factorial_negative(self):
        """
        Test whether the factorial function raises a ValueError when given a negative integer.
        """
        with self.assertRaises(ValueError):
            factorial(-5)

    def test_factorial_float(self):
        """
        Test whether the factorial function raises a TypeError when given a float.
        """
        with self.assertRaises(TypeError):
            factorial(2.5)


if __name__ == '__main__':
    """
    This code will run all the test methods defined in the TestFactorial class.
    You can run the tests by executing the test file using the command `python test_factorial.py`.
    """
    unittest.main()
