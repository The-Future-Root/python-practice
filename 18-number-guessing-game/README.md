# 18. Number guessing game

**Level:** Medium. **You'll practise:** `while` loops, the `random` module, handling bad input.

Write the classic game: the computer picks a secret number from 1 to 100, and the player keeps guessing until they get it. After each wrong guess it says whether the guess was too high or too low.

Write it as two functions, so it can be tested:

- `check_guess(guess, secret)` returns `"Too low"`, `"Too high"` or `"Correct"`.
- `play(secret)` runs one game: it keeps asking `Your guess: `, prints the hint after each guess, and when the player gets it, prints `You got it in 3 guesses!` (or `1 guess!`) and returns the number of guesses. If the player types something that isn't a whole number, it prints `Please enter a whole number` and doesn't count it as a guess.

The bottom of the file picks the secret with `random.randint(1, 100)` and calls `play`. Here's a game where the secret was 37:

```
Your guess: 50
Too high
Your guess: 25
Too low
Your guess: abc
Please enter a whole number
Your guess: 37
You got it in 3 guesses!
```

## Rules

- Keep asking until the guess is correct.
- Invalid input doesn't count as a guess.

## Test your solution

Write your code in [exercise.py](./exercise.py), then run the tests from this folder:

```bash
cd 18-number-guessing-game
python3 -m unittest -v
```

## Hints

Try for a while before you open these. Each one gives away a little more.

<details>
<summary>Hint 1</summary>

`check_guess` is three cases: `if guess < secret:` ... `elif guess > secret:` ... `else:`.

</details>

<details>
<summary>Hint 2</summary>

In `play`, use `while True:`. Read the guess inside `try`/`except ValueError`, and on an error print the message and `continue`.

</details>

<details>
<summary>Hint 3</summary>

Count only valid guesses. When `check_guess` says `"Correct"`, print the message and `return` the count. Use `"guess"` or `"guesses"` depending on the count.

</details>

## Take it further

Add a limit: the player loses after 7 wrong guesses. Is 7 enough to always win from 1 to 100? (Think about guessing the middle each time. Searching like that is called binary search.)

A full solution is in [solutions/18-number-guessing-game.py](../solutions/18-number-guessing-game.py).

Next: [19. To-do list](../19-to-do-list/)
