# Solution to 18. Number guessing game

import random


def check_guess(guess, secret):
    """Return "Too low", "Too high" or "Correct"."""
    if guess < secret:
        return "Too low"
    elif guess > secret:
        return "Too high"
    return "Correct"


def play(secret):
    """Run one game: ask "Your guess: " until it's right, print hints, and return the number of guesses."""
    guesses = 0
    while True:
        try:
            guess = int(input("Your guess: "))
        except ValueError:
            print("Please enter a whole number")
            continue
        guesses += 1
        result = check_guess(guess, secret)
        if result == "Correct":
            word = "guess" if guesses == 1 else "guesses"
            print(f"You got it in {guesses} {word}!")
            return guesses
        print(result)


if __name__ == "__main__":
    play(random.randint(1, 100))
