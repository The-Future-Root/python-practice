import unittest
from unittest import mock

import exercise
from exercise import factorial, factorial_recursive


class TestFactorial(unittest.TestCase):
    def test_loop(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(20), 2432902008176640000)

    def test_recursive(self):
        self.assertEqual(factorial_recursive(6), 720)
        self.assertEqual(factorial_recursive(0), 1)

    def test_they_agree(self):
        for n in range(15):
            self.assertEqual(factorial(n), factorial_recursive(n))

    def test_negative(self):
        for function in (factorial, factorial_recursive):
            with self.assertRaises(ValueError) as caught:
                function(-3)
            self.assertEqual(str(caught.exception), "Factorial is not defined for negative numbers")

    def test_recursive_calls_itself(self):
        with mock.patch.object(exercise, "factorial_recursive", wraps=exercise.factorial_recursive) as spy:
            spy(4)
        self.assertGreater(spy.call_count, 1, "factorial_recursive should call itself")


if __name__ == "__main__":
    unittest.main()
