import unittest

from exercise import calculate


class TestCalculate(unittest.TestCase):
    def test_four_operators(self):
        self.assertEqual(calculate(7, "+", 5), 12)
        self.assertEqual(calculate(7, "-", 10), -3)
        self.assertEqual(calculate(6, "*", 2.5), 15.0)
        self.assertEqual(calculate(9, "/", 2), 4.5)

    def test_unknown_operator(self):
        with self.assertRaises(ValueError) as caught:
            calculate(2, "^", 3)
        self.assertEqual(str(caught.exception), "Unknown operator: ^")

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError) as caught:
            calculate(5, "/", 0)
        self.assertEqual(str(caught.exception), "Cannot divide by zero")

    def test_zero_is_fine_elsewhere(self):
        self.assertEqual(calculate(0, "/", 5), 0)
        self.assertEqual(calculate(5, "*", 0), 0)


if __name__ == "__main__":
    unittest.main()
