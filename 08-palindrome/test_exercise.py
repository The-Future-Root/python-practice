import unittest

from exercise import is_palindrome


class TestPalindrome(unittest.TestCase):
    def test_simple(self):
        self.assertIs(is_palindrome("racecar"), True)
        self.assertIs(is_palindrome("hello"), False)

    def test_ignores_case(self):
        self.assertIs(is_palindrome("Racecar"), True)

    def test_ignores_spaces_and_punctuation(self):
        self.assertIs(is_palindrome("A man, a plan, a canal: Panama!"), True)
        self.assertIs(is_palindrome("Was it a car or a cat I saw?"), True)

    def test_digits(self):
        self.assertIs(is_palindrome("12321"), True)
        self.assertIs(is_palindrome("12345"), False)

    def test_empty(self):
        self.assertIs(is_palindrome(""), True)
        self.assertIs(is_palindrome("!!"), True)


if __name__ == "__main__":
    unittest.main()
