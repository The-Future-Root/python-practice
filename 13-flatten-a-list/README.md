# 13. Flatten a list

**Level:** Medium. **You'll practise:** nested loops, recursion, `isinstance`.

Data often arrives nested: a list of orders, each with a list of items. Write two functions:

- `flatten(nested)` takes a list of lists and returns one list with all their items in order, one level deep.
- `flatten_deep(nested)` handles lists nested to **any** depth, like `[1, [2, [3, [4]]]]`.

## Examples

```python
>>> flatten([[1, 2], [3], [4, 5]])
[1, 2, 3, 4, 5]
>>> flatten([['tea', 'coffee'], [], ['juice']])
['tea', 'coffee', 'juice']
>>> flatten_deep([1, [2, [3, [4]]], 5])
[1, 2, 3, 4, 5]
```

## Rules

- Keep the original order.
- In `flatten`, every item of `nested` is a list. In `flatten_deep`, items can be lists or single values.

## Test your solution

Write your code in [exercise.py](./exercise.py), then run the tests from this folder:

```bash
cd 13-flatten-a-list
python3 -m unittest -v
```

## Hints

Try for a while before you open these. Each one gives away a little more.

<details>
<summary>Hint 1</summary>

For `flatten`, use two loops: one over the inner lists, and one over the items in each.

</details>

<details>
<summary>Hint 2</summary>

For `flatten_deep`, check each item with `isinstance(item, list)`. If it's a list, it needs flattening too, and a function that calls itself does exactly that.

</details>

<details>
<summary>Hint 3</summary>

Inside `flatten_deep`, for a list item: `result.extend(flatten_deep(item))`. For anything else: `result.append(item)`.

</details>

## Take it further

Write `flatten_dict(d)`, which turns `{"a": {"b": 1, "c": {"d": 2}}}` into `{"a.b": 1, "a.c.d": 2}`. It's how nested settings are often stored in config files.

A full solution is in [solutions/13-flatten-a-list.py](../solutions/13-flatten-a-list.py).

Next: [14. Prime numbers](../14-prime-numbers/)
