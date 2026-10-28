import unittest

from exercise import reverse, reverse_words


class TestReverse(unittest.TestCase):
    def test_word(self):
        self.assertEqual(reverse("hello"), "olleh")

    def test_spaces_and_digits(self):
        self.assertEqual(reverse("Data 2026"), "6202 ataD")

    def test_empty(self):
        self.assertEqual(reverse(""), "")


class TestReverseWords(unittest.TestCase):
    def test_sentence(self):
        self.assertEqual(reverse_words("the quick fox"), "fox quick the")

    def test_extra_spaces(self):
        self.assertEqual(reverse_words("  extra   spaces here "), "here spaces extra")

    def test_one_word_and_empty(self):
        self.assertEqual(reverse_words("hello"), "hello")
        self.assertEqual(reverse_words(""), "")


if __name__ == "__main__":
    unittest.main()
