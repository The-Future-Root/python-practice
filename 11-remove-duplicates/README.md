# 11. Remove duplicates

**Level:** Easy. **You'll practise:** building a new list, checking membership.

A mailing list has the same email address several times, or a list of orders has repeated product codes. Write `remove_duplicates(items)`, which returns a **new** list with each item only once, keeping the first copy of each and the original order.

The original list must not change.

## Examples

```python
>>> remove_duplicates([3, 1, 3, 2, 1])
[3, 1, 2]
>>> remove_duplicates(['tea', 'coffee', 'tea', 'juice'])
['tea', 'coffee', 'juice']
>>> remove_duplicates([])
[]
```

## Rules

- Keep the first copy of each item, and keep the original order.
- Don't change the list you were given.

## Test your solution

Write your code in [exercise.py](./exercise.py), then run the tests from this folder:

```bash
cd 11-remove-duplicates
python3 -m unittest -v
```

## Hints

Try for a while before you open these. Each one gives away a little more.

<details>
<summary>Hint 1</summary>

Build a new list instead of removing items from the old one. Changing a list while you loop over it makes the loop skip items.

</details>

<details>
<summary>Hint 2</summary>

Keep a list called `seen`. For each item, `if item not in seen:`, append it.

</details>

<details>
<summary>Hint 3</summary>

`seen` is also your answer: return it. (`list(set(items))` removes duplicates too, but it loses the order.)

</details>

## Take it further

Write `remove_duplicates_ignore_case(words)`, so that `"Tea"` and `"tea"` count as the same word, keeping whichever spelling came first.

A full solution is in [solutions/11-remove-duplicates.py](../solutions/11-remove-duplicates.py).

Next: [12. Second largest](../12-second-largest/)
