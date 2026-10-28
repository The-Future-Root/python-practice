# 15. Factorial

**Level:** Easy. **You'll practise:** loops, recursion, raising errors.

The **factorial** of a whole number `n`, written `n!`, is every number from 1 to `n` multiplied together: 5! = 5 × 4 × 3 × 2 × 1 = 120. It counts the number of ways to arrange things: 5 people can stand in a queue in 120 different orders. By definition, 0! is 1.

Write it twice:

- `factorial(n)` with a loop.
- `factorial_recursive(n)` with recursion: a function that calls itself, using the fact that `n! = n × (n - 1)!`.

Factorials of negative numbers don't exist, so both raise `ValueError` with the message `Factorial is not defined for negative numbers`.

## Examples

```python
>>> factorial(5)
120
>>> factorial(0)
1
>>> factorial_recursive(6)
720
>>> factorial(20)
2432902008176640000
```

## Rules

- `factorial(0)` and `factorial_recursive(0)` both return 1.
- `factorial_recursive` must call itself.

## Test your solution

Write your code in [exercise.py](./exercise.py), then run the tests from this folder:

```bash
cd 15-factorial
python3 -m unittest -v
```

## Hints

Try for a while before you open these. Each one gives away a little more.

<details>
<summary>Hint 1</summary>

For the loop version, start a result at **1** (not 0, or everything multiplies to 0), and multiply it by each number from 1 to `n`.

</details>

<details>
<summary>Hint 2</summary>

Every recursive function needs a **base case** that stops it: when `n` is 0, return 1.

</details>

<details>
<summary>Hint 3</summary>

Otherwise, `return n * factorial_recursive(n - 1)`. Check for negative `n` first in both functions.

</details>

## Take it further

Try `factorial_recursive(5000)`. Python stops with a `RecursionError`, because each call waits for the next one and Python limits how deep that can go. The loop version has no such limit. That's a real trade-off of recursion.

A full solution is in [solutions/15-factorial.py](../solutions/15-factorial.py).

Next: [16. Caesar cipher](../16-caesar-cipher/)
