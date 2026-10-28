# 7. Count vowels

**Level:** Easy. **You'll practise:** loops over strings, `in`, dictionaries for counting.

Write two functions:

- `count_vowels(text)` returns how many vowels (a, e, i, o, u) the text has, in upper or lower case.
- `vowel_counts(text)` returns a dictionary with a count for **each** vowel, including the ones that don't appear.

## Examples

```python
>>> count_vowels('Hello World')
3
>>> count_vowels('AEIOU aeiou')
10
>>> vowel_counts('Programming is fun')
{'a': 1, 'e': 0, 'i': 2, 'o': 1, 'u': 1}
>>> vowel_counts('Rhythm')
{'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
```

## Rules

- Count only a, e, i, o and u. Treat `y` as a consonant.
- The dictionary always has all five keys, in the order a, e, i, o, u.

## Test your solution

Write your code in [exercise.py](./exercise.py), then run the tests from this folder:

```bash
cd 07-count-vowels
python3 -m unittest -v
```

## Hints

Try for a while before you open these. Each one gives away a little more.

<details>
<summary>Hint 1</summary>

Lowercase the text first with `text.lower()`, so you only check for lowercase vowels.

</details>

<details>
<summary>Hint 2</summary>

In `count_vowels`, loop over the characters and add 1 whenever `char in "aeiou"`.

</details>

<details>
<summary>Hint 3</summary>

Start `vowel_counts` with `counts = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}`, then do `counts[char] += 1` when `char in counts`.

</details>

## Take it further

Write `most_common_letter(text)`, which counts every letter (not just vowels) and returns the most common one.

A full solution is in [solutions/07-count-vowels.py](../solutions/07-count-vowels.py).

Next: [8. Palindrome check](../08-palindrome/)
