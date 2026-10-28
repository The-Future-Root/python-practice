# 18. Number guessing game
#
# The problem, examples and rules are in README.md.
# Test with:  python3 -m unittest -v

import random


def check_guess(guess, secret):
    """Return "Too low", "Too high" or "Correct"."""
    pass


def play(secret):
    """Run one game: ask "Your guess: " until it's right, print hints, and return the number of guesses."""
    pass


if __name__ == "__main__":
    play(random.randint(1, 100))
