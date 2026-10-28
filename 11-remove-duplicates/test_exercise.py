import unittest

from exercise import remove_duplicates


class TestRemoveDuplicates(unittest.TestCase):
    def test_numbers(self):
        self.assertEqual(remove_duplicates([1, 2, 3, 2, 1, 4]), [1, 2, 3, 4])

    def test_keeps_first_seen_order(self):
        self.assertEqual(remove_duplicates([3, 1, 3, 2, 1]), [3, 1, 2])

    def test_strings(self):
        self.assertEqual(remove_duplicates(["tea", "coffee", "tea", "juice"]), ["tea", "coffee", "juice"])

    def test_original_unchanged(self):
        original = [5, 5, 6]
        remove_duplicates(original)
        self.assertEqual(original, [5, 5, 6], "Return a new list; don't change the one you were given")

    def test_empty(self):
        self.assertEqual(remove_duplicates([]), [])


if __name__ == "__main__":
    unittest.main()
