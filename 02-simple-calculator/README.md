# 2. Simple calculator

**Level:** Easy. **You'll practise:** functions, `if`/`elif`, raising exceptions.

Write a function `calculate(a, operator, b)` that works like a basic calculator. `operator` is one of `"+"`, `"-"`, `"*"` or `"/"`.

A real calculator mustn't crash or give nonsense when it's misused, so the function has to deal with two problems: an operator it doesn't know, and division by zero.

## Examples

```python
>>> calculate(7, '+', 5)
12
>>> calculate(7, '-', 10)
-3
>>> calculate(6, '*', 2.5)
15.0
>>> calculate(9, '/', 2)
4.5
```

## Rules

- Return the result of the calculation.
- For an operator that isn't one of the four, raise `ValueError` with the message `Unknown operator: ^` (with the actual operator).
- For division by zero, raise `ZeroDivisionError` with the message `Cannot divide by zero`.

## Test your solution

Write your code in [exercise.py](./exercise.py), then run the tests from this folder:

```bash
cd 02-simple-calculator
python3 -m unittest -v
```

## Hints

Try for a while before you open these. Each one gives away a little more.

<details>
<summary>Hint 1</summary>

Use `if`/`elif` to check which operator you have, and `return` the matching calculation.

</details>

<details>
<summary>Hint 2</summary>

After the four `elif`s, an `else:` can `raise ValueError(f"Unknown operator: {operator}")`.

</details>

<details>
<summary>Hint 3</summary>

Check `b == 0` inside the `/` branch, before dividing, and `raise ZeroDivisionError("Cannot divide by zero")`.

</details>

## Take it further

Add `**` (power) and `%` (remainder). Then write a small program around the function that asks for the two numbers and the operator, and prints the answer or the error message.

A full solution is in [solutions/02-simple-calculator.py](../solutions/02-simple-calculator.py).

Next: [3. Even or odd](../03-even-or-odd/)
