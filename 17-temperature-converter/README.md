# 17. Temperature converter

**Level:** Medium. **You'll practise:** formulas, validating input, organising conversions.

Write `convert(value, from_unit, to_unit)`, which converts a temperature between Celsius (`"C"`), Fahrenheit (`"F"`) and Kelvin (`"K"`), and returns the result rounded to 2 decimal places.

| From | To | Formula |
|---|---|---|
| Celsius | Fahrenheit | F = C × 9/5 + 32 |
| Fahrenheit | Celsius | C = (F - 32) × 5/9 |
| Celsius | Kelvin | K = C + 273.15 |

Accept the units in either case: `"c"` and `"C"` both mean Celsius. For a unit that isn't C, F or K, raise `ValueError` with the message `Unknown unit: X`. Nothing can be colder than absolute zero (0 K, which is -273.15 °C), so for a temperature below that, raise `ValueError` with the message `Below absolute zero`.

## Examples

```python
>>> convert(100, 'C', 'F')
212.0
>>> convert(98.6, 'f', 'c')
37.0
>>> convert(0, 'C', 'K')
273.15
>>> convert(-40, 'F', 'C')
-40.0
>>> convert(20, 'C', 'C')
20
```

## Rules

- Round the result to 2 decimal places.
- Check the units before anything else, then check for absolute zero.

## Test your solution

Write your code in [exercise.py](./exercise.py), then run the tests from this folder:

```bash
cd 17-temperature-converter
python3 -m unittest -v
```

## Hints

Try for a while before you open these. Each one gives away a little more.

<details>
<summary>Hint 1</summary>

Rather than writing a formula for every pair of units (six of them), convert everything to Celsius first, then from Celsius to the unit you want. That's only four small formulas.

</details>

<details>
<summary>Hint 2</summary>

Tidy the units with `.upper()`, then check them with `if unit not in ("C", "F", "K"):`.

</details>

<details>
<summary>Hint 3</summary>

Once you have the value in Celsius, `if celsius < -273.15:` catches values below absolute zero, whichever unit they arrived in.

</details>

## Take it further

Make it a program: read lines like `100 C F` from the user, print the answer, and keep going until they type `quit`.

A full solution is in [solutions/17-temperature-converter.py](../solutions/17-temperature-converter.py).

Next: [18. Number guessing game](../18-number-guessing-game/)
