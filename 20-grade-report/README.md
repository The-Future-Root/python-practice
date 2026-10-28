# 20. Grade report

**Level:** Harder. **You'll practise:** dictionaries of lists, sorting by more than one thing, functions working together.

A teacher has every student's test scores in a dictionary, and wants a report. Write three functions:

- `letter_grade(average)` returns `"A"` for 90 and above, `"B"` for 80 to just under 90, `"C"` for 70 to just under 80, `"D"` for 60 to just under 70, and `"F"` below 60.
- `average(scores)` returns the average of a list of scores, rounded to 1 decimal place, or `None` for an empty list.
- `report(students)` takes a dictionary of student name to list of scores, and returns a list of `(name, average, grade)` tuples, **highest average first**. Students with the same average are listed alphabetically. Students with no scores are left out.

## Examples

```python
>>> letter_grade(89.9)
'B'
>>> average([85, 92, 78])
85.0
>>> report({'Sam': [70, 75, 80], 'Alex': [92, 88, 95], 'Priya': [80, 70, 75], 'Jo': []})
[('Alex', 91.7, 'A'), ('Priya', 75.0, 'C'), ('Sam', 75.0, 'C')]
```

## Rules

- The boundaries are exact: 90 is an A, 89.9 is a B.
- Use the rounded average to choose the grade.

## Test your solution

Write your code in [exercise.py](./exercise.py), then run the tests from this folder:

```bash
cd 20-grade-report
python3 -m unittest -v
```

## Hints

Try for a while before you open these. Each one gives away a little more.

<details>
<summary>Hint 1</summary>

`letter_grade` is an `if`/`elif` chain. Check the highest grade first.

</details>

<details>
<summary>Hint 2</summary>

In `report`, build a list of tuples with `results.append((name, avg, letter_grade(avg)))`, skipping students whose average is `None`.

</details>

<details>
<summary>Hint 3</summary>

To sort by average (highest first) and then by name, sort with a key that returns both: `results.sort(key=lambda r: (-r[1], r[0]))`. The minus sign puts high averages first while the names stay A to Z.

</details>

## Take it further

Print the report as a neat table with f-string alignment, and add a line at the bottom with the class average and how many students got each grade.

A full solution is in [solutions/20-grade-report.py](../solutions/20-grade-report.py).

Next: you've finished the set. Well done.
