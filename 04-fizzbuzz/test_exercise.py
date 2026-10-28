import unittest

from exercise import fizzbuzz


class TestFizzBuzz(unittest.TestCase):
    def test_first_fifteen(self):
        self.assertEqual(fizzbuzz(15), ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz",
                                        "11", "Fizz", "13", "14", "FizzBuzz"])

    def test_length(self):
        self.assertEqual(len(fizzbuzz(100)), 100)

    def test_later_numbers(self):
        result = fizzbuzz(100)
        self.assertEqual(result[89], "FizzBuzz")  # 90
        self.assertEqual(result[98], "Fizz")      # 99
        self.assertEqual(result[99], "Buzz")      # 100
        self.assertEqual(result[96], "97")

    def test_zero(self):
        self.assertEqual(fizzbuzz(0), [])

    def test_strings_not_numbers(self):
        self.assertEqual(fizzbuzz(1), ["1"], "Plain numbers should be strings, like \"1\"")


if __name__ == "__main__":
    unittest.main()
