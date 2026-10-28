import unittest

from exercise import describe, is_even


class TestEvenOrOdd(unittest.TestCase):
    def test_is_even(self):
        self.assertIs(is_even(10), True)
        self.assertIs(is_even(7), False)

    def test_zero_and_negatives(self):
        self.assertIs(is_even(0), True)
        self.assertIs(is_even(-4), True)
        self.assertIs(is_even(-3), False)

    def test_describe(self):
        self.assertEqual(describe(7), "7 is odd")
        self.assertEqual(describe(10), "10 is even")
        self.assertEqual(describe(0), "0 is even")


if __name__ == "__main__":
    unittest.main()
