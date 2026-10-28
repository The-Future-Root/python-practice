import unittest

from exercise import flatten, flatten_deep


class TestFlatten(unittest.TestCase):
    def test_numbers(self):
        self.assertEqual(flatten([[1, 2], [3], [4, 5]]), [1, 2, 3, 4, 5])

    def test_empty_inner_lists(self):
        self.assertEqual(flatten([["tea", "coffee"], [], ["juice"]]), ["tea", "coffee", "juice"])

    def test_one_level_only(self):
        self.assertEqual(flatten([[1, [2]], [3]]), [1, [2], 3])

    def test_empty(self):
        self.assertEqual(flatten([]), [])


class TestFlattenDeep(unittest.TestCase):
    def test_deep(self):
        self.assertEqual(flatten_deep([1, [2, [3, [4]]], 5]), [1, 2, 3, 4, 5])

    def test_already_flat(self):
        self.assertEqual(flatten_deep([1, 2, 3]), [1, 2, 3])

    def test_strings_are_not_split(self):
        self.assertEqual(flatten_deep(["ab", ["cd", ["ef"]]]), ["ab", "cd", "ef"])


if __name__ == "__main__":
    unittest.main()
