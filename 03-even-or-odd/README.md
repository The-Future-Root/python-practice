# 3. Even or odd

**Level:** Easy. **You'll practise:** the `%` operator, returning text.

Write two functions:

- `is_even(n)` returns `True` if the whole number `n` is even, and `False` if it's odd.
- `describe(n)` returns a sentence like `"7 is odd"` or `"10 is even"`, using `is_even`.

Zero is even, and so are negative numbers like -4.

## Examples

```python
>>> is_even(10)
True
>>> is_even(7)
False
>>> describe(7)
'7 is odd'
>>> describe(0)
'0 is even'
>>> describe(-4)
'-4 is even'
```

## Rules

- `is_even` returns a bool, not text.
- `describe` should call `is_even` rather than repeat the check.

## Test your solution

Write your code in [exercise.py](./exercise.py), then run the tests from this folder:

```bash
cd 03-even-or-odd
python3 -m unittest -v
```

## Hints

Try for a while before you open these. Each one gives away a little more.

<details>
<summary>Hint 1</summary>

A number is even when dividing it by 2 leaves no remainder.

</details>

<details>
<summary>Hint 2</summary>

`n % 2` is the remainder after dividing by 2. It's `0` for even numbers.

</details>

<details>
<summary>Hint 3</summary>

`return n % 2 == 0` is the whole of `is_even`. In `describe`, use `if is_even(n):` to choose the word.

</details>

## Take it further

Write `split_even_odd(numbers)`, which takes a list of numbers and returns two lists: the even ones and the odd ones.

A full solution is in [solutions/03-even-or-odd.py](../solutions/03-even-or-odd.py).

Next: [4. FizzBuzz](../04-fizzbuzz/)
