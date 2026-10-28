# 4. FizzBuzz

**Level:** Easy. **You'll practise:** loops, `%`, the order of `if` checks.

FizzBuzz is a famous programming exercise, and still a common first question in job interviews. Write `fizzbuzz(n)`, which returns a list of strings for the numbers from 1 to `n`:

- for multiples of 3, the string `"Fizz"`
- for multiples of 5, the string `"Buzz"`
- for multiples of both 3 and 5, the string `"FizzBuzz"`
- for every other number, the number itself as a string, like `"7"`

## Examples

```python
>>> fizzbuzz(5)
['1', '2', 'Fizz', '4', 'Buzz']
>>> fizzbuzz(15)[-5:]
['11', 'Fizz', '13', '14', 'FizzBuzz']
```

## Rules

- Return a list with exactly `n` strings.
- `fizzbuzz(0)` returns an empty list.

## Test your solution

Write your code in [exercise.py](./exercise.py), then run the tests from this folder:

```bash
cd 04-fizzbuzz
python3 -m unittest -v
```

## Hints

Try for a while before you open these. Each one gives away a little more.

<details>
<summary>Hint 1</summary>

Loop with `for number in range(1, n + 1):` so that `n` itself is included.

</details>

<details>
<summary>Hint 2</summary>

Check the FizzBuzz case first. If you check for 3 first, 15 becomes `"Fizz"` and never reaches the FizzBuzz check.

</details>

<details>
<summary>Hint 3</summary>

A multiple of both 3 and 5 is a multiple of 15: `if number % 15 == 0:`. Use `str(number)` for the plain numbers.

</details>

## Take it further

Make the words and divisors configurable: `fizzbuzz(n, {3: "Fizz", 5: "Buzz", 7: "Bazz"})`, so 21 becomes `"FizzBazz"`.

A full solution is in [solutions/04-fizzbuzz.py](../solutions/04-fizzbuzz.py).

Next: [5. Sum of 1 to n](../05-sum-to-n/)
