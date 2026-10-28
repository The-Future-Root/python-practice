import ast
import pathlib
import unittest

from exercise import sum_formula, sum_to

SOURCE = pathlib.Path(__file__).with_name("exercise.py").read_text()


class TestSumToN(unittest.TestCase):
    def test_loop_version(self):
        self.assertEqual(sum_to(5), 15)
        self.assertEqual(sum_to(100), 5050)
        self.assertEqual(sum_to(1), 1)

    def test_formula_version(self):
        self.assertEqual(sum_formula(100), 5050)
        self.assertIsInstance(sum_formula(100), int, "Use // so the result is an int")

    def test_they_agree(self):
        for n in range(1, 60):
            self.assertEqual(sum_to(n), sum_formula(n), f"Different answers for n = {n}")

    def test_less_than_one(self):
        for n in (0, -5):
            self.assertEqual(sum_to(n), 0)
            self.assertEqual(sum_formula(n), 0)

    def test_loop_doesnt_use_sum(self):
        for node in ast.walk(ast.parse(SOURCE)):
            if isinstance(node, ast.FunctionDef) and node.name == "sum_to":
                calls = {n.func.id for n in ast.walk(node) if isinstance(n, ast.Call) and isinstance(n.func, ast.Name)}
                self.assertNotIn("sum", calls, "Write the loop yourself in sum_to, without sum()")


if __name__ == "__main__":
    unittest.main()
