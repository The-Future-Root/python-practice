import unittest

from exercise import second_largest


class TestSecondLargest(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(second_largest([3, 7, 1, 9, 4]), 7)

    def test_duplicates_of_largest(self):
        self.assertEqual(second_largest([9, 9, 4]), 4)
        self.assertEqual(second_largest([4, 9, 9]), 4)

    def test_largest_first(self):
        self.assertEqual(second_largest([10, 3]), 3)

    def test_negatives(self):
        self.assertEqual(second_largest([-2, -8, -5]), -5)

    def test_not_enough_values(self):
        self.assertIsNone(second_largest([5, 5, 5]))
        self.assertIsNone(second_largest([1]))
        self.assertIsNone(second_largest([]))

    def test_original_unchanged(self):
        original = [3, 1, 2]
        second_largest(original)
        self.assertEqual(original, [3, 1, 2])


if __name__ == "__main__":
    unittest.main()
