import io
import unittest
from contextlib import redirect_stdout
from unittest import mock

from exercise import check_guess, play


def play_with(secret, *answers):
    output = io.StringIO()
    with mock.patch("builtins.input", side_effect=list(answers)), redirect_stdout(output):
        count = play(secret)
    return count, output.getvalue()


class TestCheckGuess(unittest.TestCase):
    def test_hints(self):
        self.assertEqual(check_guess(20, 37), "Too low")
        self.assertEqual(check_guess(50, 37), "Too high")
        self.assertEqual(check_guess(37, 37), "Correct")


class TestPlay(unittest.TestCase):
    def test_three_guesses(self):
        count, output = play_with(37, "50", "25", "37")
        self.assertEqual(count, 3)
        self.assertIn("Too high", output)
        self.assertIn("Too low", output)
        self.assertIn("You got it in 3 guesses!", output)

    def test_first_time(self):
        count, output = play_with(10, "10")
        self.assertEqual(count, 1)
        self.assertIn("You got it in 1 guess!", output)

    def test_bad_input_not_counted(self):
        count, output = play_with(5, "five", "", "5")
        self.assertEqual(count, 1, "Invalid input shouldn't count as a guess")
        self.assertEqual(output.count("Please enter a whole number"), 2)


if __name__ == "__main__":
    unittest.main()
