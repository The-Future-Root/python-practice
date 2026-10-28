import unittest

from exercise import count_vowels, vowel_counts


class TestCountVowels(unittest.TestCase):
    def test_mixed_case(self):
        self.assertEqual(count_vowels("Hello World"), 3)
        self.assertEqual(count_vowels("AEIOU aeiou"), 10)

    def test_no_vowels(self):
        self.assertEqual(count_vowels("Rhythm"), 0)
        self.assertEqual(count_vowels(""), 0)


class TestVowelCounts(unittest.TestCase):
    def test_counts(self):
        self.assertEqual(vowel_counts("Programming is fun"), {"a": 1, "e": 0, "i": 2, "o": 1, "u": 1})

    def test_all_zero(self):
        self.assertEqual(vowel_counts("Rhythm"), {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0})

    def test_uppercase(self):
        self.assertEqual(vowel_counts("EEE")["e"], 3)


if __name__ == "__main__":
    unittest.main()
