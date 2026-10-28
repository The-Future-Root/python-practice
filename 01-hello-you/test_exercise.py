import pathlib
import subprocess
import sys
import unittest

PROGRAM = pathlib.Path(__file__).with_name("exercise.py")


def run(*answers):
    result = subprocess.run([sys.executable, str(PROGRAM)], input="\n".join(answers) + "\n",
                            capture_output=True, text=True, timeout=10)
    return result.stdout + result.stderr


class TestHelloYou(unittest.TestCase):
    def test_prompts(self):
        output = run("Alex", "Kim")
        self.assertIn("First name: ", output)
        self.assertIn("Last name: ", output)

    def test_greeting(self):
        self.assertIn("Hello, Alex Kim! Nice to meet you.", run("Alex", "Kim"))

    def test_tidies_names(self):
        self.assertIn("Hello, Priya Shah! Nice to meet you.", run("  priya ", "SHAH  "))

    def test_two_word_last_name(self):
        self.assertIn("Hello, Maria Del Rio! Nice to meet you.", run("maria", "del rio"))


if __name__ == "__main__":
    unittest.main()
