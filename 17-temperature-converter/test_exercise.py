import unittest

from exercise import convert


class TestConvert(unittest.TestCase):
    def test_c_to_f(self):
        self.assertEqual(convert(100, "C", "F"), 212.0)
        self.assertEqual(convert(0, "C", "F"), 32.0)

    def test_f_to_c(self):
        self.assertEqual(convert(98.6, "F", "C"), 37.0)
        self.assertEqual(convert(-40, "F", "C"), -40.0)

    def test_kelvin(self):
        self.assertEqual(convert(0, "C", "K"), 273.15)
        self.assertEqual(convert(0, "K", "F"), -459.67)
        self.assertEqual(convert(300, "K", "C"), 26.85)

    def test_lowercase_units(self):
        self.assertEqual(convert(98.6, "f", "c"), 37.0)

    def test_same_unit(self):
        self.assertEqual(convert(20, "C", "C"), 20)

    def test_unknown_unit(self):
        with self.assertRaises(ValueError) as caught:
            convert(10, "C", "X")
        self.assertEqual(str(caught.exception), "Unknown unit: X")

    def test_below_absolute_zero(self):
        for value, unit in ((-300, "C"), (-1, "K"), (-500, "F")):
            with self.assertRaises(ValueError) as caught:
                convert(value, unit, "C")
            self.assertEqual(str(caught.exception), "Below absolute zero")


if __name__ == "__main__":
    unittest.main()
