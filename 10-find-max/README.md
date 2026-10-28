# 10. Find the max

**Level:** Easy. **You'll practise:** tracking the best value in a loop.

Python has `max()` and `min()`, but every programmer should be able to write them. It's the same pattern you'll use for "the cheapest flight" or "the customer who spent the most". Write three functions, **without** using `max()`, `min()` or `sorted()`:

- `find_max(numbers)` returns the largest number.
- `find_min(numbers)` returns the smallest number.
- `find_average(numbers)` returns the average, rounded to 2 decimal places.

All three return `None` for an empty list.

## Examples

```python
>>> find_max([3, 7, 1, 9, 4])
9
>>> find_max([-5, -1, -8])
-1
>>> find_min([3, 7, 1, 9, 4])
1
>>> find_average([3, 7, 1, 9, 4])
4.8
>>> find_max([])
None
```

## Rules

- Don't use `max()`, `min()` or `sorted()`.
- Return `None` for an empty list.

## Test your solution

Write your code in [exercise.py](./exercise.py), then run the tests from this folder:

```bash
cd 10-find-max
python3 -m unittest -v
```

## Hints

Try for a while before you open these. Each one gives away a little more.

<details>
<summary>Hint 1</summary>

Don't start with `biggest = 0`: for a list of negative numbers, you'd wrongly return 0.

</details>

<details>
<summary>Hint 2</summary>

Start with the first item, `biggest = numbers[0]`, then loop over the rest and replace it whenever you see something bigger.

</details>

<details>
<summary>Hint 3</summary>

For the average, `sum(numbers) / len(numbers)` is fine to use. Check for an empty list first, or `len()` will be 0 and you'll divide by zero.

</details>

## Take it further

Write `find_max_by(items, key)`, which finds the dictionary in a list with the biggest value for a given key, like the most expensive product in `[{"name": "Pen", "price": 1.5}, ...]`.

A full solution is in [solutions/10-find-max.py](../solutions/10-find-max.py).

Next: [11. Remove duplicates](../11-remove-duplicates/)
