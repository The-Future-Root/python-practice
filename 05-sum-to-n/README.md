# 5. Sum of 1 to n

**Level:** Easy. **You'll practise:** loops, accumulators, a maths shortcut.

Write two functions that add up all the whole numbers from 1 to `n`. For example, for 5 that's 1 + 2 + 3 + 4 + 5 = 15.

- `sum_to(n)` uses a loop.
- `sum_formula(n)` uses the formula `n * (n + 1) // 2` instead.

Both must give the same answer. If `n` is less than 1, both return 0.

The story goes that the mathematician Gauss worked out the formula as a schoolboy, when his teacher set the class the job of adding up 1 to 100. Pair the numbers up from both ends, 1 + 100, 2 + 99, 3 + 98, and every pair makes 101. There are 50 pairs, so the total is 5050.

## Examples

```python
>>> sum_to(5)
15
>>> sum_to(100)
5050
>>> sum_formula(100)
5050
>>> sum_formula(1_000_000)
500000500000
```

## Rules

- Both return a whole number (`int`), not a float.
- Don't use Python's `sum()` in `sum_to`: the point is to write the loop.

## Test your solution

Write your code in [exercise.py](./exercise.py), then run the tests from this folder:

```bash
cd 05-sum-to-n
python3 -m unittest -v
```

## Hints

Try for a while before you open these. Each one gives away a little more.

<details>
<summary>Hint 1</summary>

Start a total at 0 and add each number to it, in a loop over `range(1, n + 1)`.

</details>

<details>
<summary>Hint 2</summary>

Use `//` in the formula, not `/`. `/` always gives a float, like `15.0`.

</details>

<details>
<summary>Hint 3</summary>

For `n` less than 1, the loop doesn't run at all, so `sum_to` returns 0 with no extra code. `sum_formula` needs an `if`.

</details>

## Take it further

Time both functions for `n = 10_000_000` with the `time` module. The loop takes about a second; the formula is instant. That difference is what lesson 1 of the data structures course, Big O, is about.

A full solution is in [solutions/05-sum-to-n.py](../solutions/05-sum-to-n.py).

Next: [6. Reverse text](../06-reverse-text/)
