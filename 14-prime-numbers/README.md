# 14. Prime numbers

**Level:** Medium. **You'll practise:** loops with early exits, making code faster.

A **prime number** is a whole number above 1 whose only divisors are 1 and itself: 2, 3, 5, 7, 11, 13... Primes are behind the encryption that protects online banking.

Write two functions:

- `is_prime(n)` returns `True` if `n` is prime.
- `primes_up_to(limit)` returns a list of every prime from 2 up to and including `limit`.

`is_prime` must be quick even for big numbers like 1,000,003.

## Examples

```python
>>> is_prime(7)
True
>>> is_prime(9)
False
>>> is_prime(1)
False
>>> primes_up_to(30)
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
```

## Rules

- Numbers below 2 aren't prime.
- `primes_up_to` includes `limit` itself if it's prime.

## Test your solution

Write your code in [exercise.py](./exercise.py), then run the tests from this folder:

```bash
cd 14-prime-numbers
python3 -m unittest -v
```

## Hints

Try for a while before you open these. Each one gives away a little more.

<details>
<summary>Hint 1</summary>

Handle `n < 2` first: return `False`. Then try dividing by every number from 2 upwards; if any divides exactly (`n % d == 0`), it isn't prime.

</details>

<details>
<summary>Hint 2</summary>

You only need to try divisors up to the square root of `n`. If `n` had a factor bigger than that, it would also have one smaller. Loop `while d * d <= n:`.

</details>

<details>
<summary>Hint 3</summary>

`primes_up_to` can reuse `is_prime`: `[n for n in range(2, limit + 1) if is_prime(n)]`.

</details>

## Take it further

Look up the **Sieve of Eratosthenes**, a much faster way to find all the primes up to a limit, and write `sieve(limit)`. Compare its speed with `primes_up_to` for a limit of a million.

A full solution is in [solutions/14-prime-numbers.py](../solutions/14-prime-numbers.py).

Next: [15. Factorial](../15-factorial/)
