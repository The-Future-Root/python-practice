import ast
import pathlib
import unittest

from exercise import find_average, find_max, find_min

SOURCE = pathlib.Path(__file__).with_name("exercise.py").read_text()


class TestFindMax(unittest.TestCase):
    def test_max(self):
        self.assertEqual(find_max([3, 7, 1, 9, 4]), 9)

    def test_all_negative(self):
        self.assertEqual(find_max([-5, -1, -8]), -1, "Don't start biggest at 0")

    def test_min(self):
        self.assertEqual(find_min([3, 7, 1, 9, 4]), 1)
        self.assertEqual(find_min([5]), 5)

    def test_average(self):
        self.assertEqual(find_average([3, 7, 1, 9, 4]), 4.8)
        self.assertEqual(find_average([1, 2]), 1.5)
        self.assertEqual(find_average([1, 1, 2]), 1.33)

    def test_empty(self):
        self.assertIsNone(find_max([]))
        self.assertIsNone(find_min([]))
        self.assertIsNone(find_average([]))

    def test_no_builtins(self):
        names = {n.func.id for n in ast.walk(ast.parse(SOURCE)) if isinstance(n, ast.Call) and isinstance(n.func, ast.Name)}
        for builtin in ("max", "min", "sorted"):
            self.assertNotIn(builtin, names, f"Find it with a loop instead of {builtin}()")


if __name__ == "__main__":
    unittest.main()
