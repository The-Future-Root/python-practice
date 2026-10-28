# 12. Second largest

**Level:** Medium. **You'll practise:** tracking two values at once, edge cases.

Write `second_largest(numbers)`, which returns the second largest **distinct** value in a list. In `[3, 7, 1, 9, 4]` that's 7. In `[9, 9, 4]` it's 4, because the second 9 isn't a different value.

If there are fewer than two distinct values, return `None`.

Try to do it in a single pass through the list, without sorting. It's a common interview question for exactly that reason.

## Examples

```python
>>> second_largest([3, 7, 1, 9, 4])
7
>>> second_largest([9, 9, 4])
4
>>> second_largest([5, 5, 5])
None
>>> second_largest([-2, -8, -5])
-5
```

## Rules

- Return `None` when there are fewer than two distinct values.
- Don't change the list you were given.

## Test your solution

Write your code in [exercise.py](./exercise.py), then run the tests from this folder:

```bash
cd 12-second-largest
python3 -m unittest -v
```

## Hints

Try for a while before you open these. Each one gives away a little more.

<details>
<summary>Hint 1</summary>

Keep two variables, `largest` and `second`, both starting at `None`.

</details>

<details>
<summary>Hint 2</summary>

For each number: if it's bigger than `largest`, the old `largest` becomes `second` and the number becomes `largest`. Otherwise, if it's bigger than `second` (or `second` is `None`), it becomes `second`.

</details>

<details>
<summary>Hint 3</summary>

Skip any number equal to `largest`, or `[9, 9, 4]` gives 9.

</details>

## Take it further

Generalise it: `nth_largest(numbers, n)`. Then think about which is better for big lists, your approach or `sorted(set(numbers))`.

A full solution is in [solutions/12-second-largest.py](../solutions/12-second-largest.py).

Next: [13. Flatten a list](../13-flatten-a-list/)
