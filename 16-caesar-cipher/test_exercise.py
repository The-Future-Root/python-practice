import unittest

from exercise import decrypt, encrypt


class TestCaesar(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(encrypt("hello", 3), "khoor")

    def test_wraps_round(self):
        self.assertEqual(encrypt("xyz", 3), "abc")

    def test_keeps_case_and_other_characters(self):
        self.assertEqual(encrypt("Meet at 10pm!", 5), "Rjjy fy 10ur!")

    def test_big_and_negative_shifts(self):
        self.assertEqual(encrypt("abc", 29), "def")
        self.assertEqual(encrypt("def", -3), "abc")

    def test_decrypt(self):
        self.assertEqual(decrypt("Rjjy fy 10ur!", 5), "Meet at 10pm!")

    def test_round_trip(self):
        message = "Attack at dawn, then retreat to the hills."
        for shift in (1, 7, 13, 25, 40):
            self.assertEqual(decrypt(encrypt(message, shift), shift), message)


if __name__ == "__main__":
    unittest.main()
