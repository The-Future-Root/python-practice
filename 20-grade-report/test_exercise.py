import unittest

from exercise import average, letter_grade, report


class TestLetterGrade(unittest.TestCase):
    def test_boundaries(self):
        cases = {100: "A", 90: "A", 89.9: "B", 80: "B", 79.9: "C", 70: "C", 69.9: "D", 60: "D", 59.9: "F", 0: "F"}
        for score, grade in cases.items():
            self.assertEqual(letter_grade(score), grade, f"{score} should be {grade}")


class TestAverage(unittest.TestCase):
    def test_average(self):
        self.assertEqual(average([85, 92, 78]), 85.0)
        self.assertEqual(average([90, 91, 91]), 90.7)

    def test_empty(self):
        self.assertIsNone(average([]))


class TestReport(unittest.TestCase):
    def test_order_and_grades(self):
        students = {"Sam": [70, 75, 80], "Alex": [92, 88, 95], "Priya": [80, 70, 75], "Jo": []}
        self.assertEqual(report(students), [("Alex", 91.7, "A"), ("Priya", 75.0, "C"), ("Sam", 75.0, "C")])

    def test_ties_alphabetical(self):
        students = {"Zoe": [80], "Ann": [80], "Max": [95]}
        self.assertEqual([r[0] for r in report(students)], ["Max", "Ann", "Zoe"])

    def test_empty(self):
        self.assertEqual(report({}), [])


if __name__ == "__main__":
    unittest.main()
