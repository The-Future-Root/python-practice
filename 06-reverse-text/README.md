# 6. Reverse text

**Level:** Easy. **You'll practise:** loops over strings, slicing, `split` and `join`.

Write two functions:

- `reverse(text)` returns the text backwards: `"hello"` becomes `"olleh"`.
- `reverse_words(sentence)` keeps each word the same, but reverses their order: `"the quick fox"` becomes `"fox quick the"`.

Try `reverse` with a loop first, building the result one character at a time. Then try the one-line slicing version.

## Examples

```python
>>> reverse('hello')
'olleh'
>>> reverse('Data 2026')
'6202 ataD'
>>> reverse_words('the quick fox')
'fox quick the'
>>> reverse_words('  extra   spaces here ')
'here spaces extra'
```

## Rules

- An empty string returns an empty string.
- In `reverse_words`, words are separated by single spaces in the result, whatever spacing the input had.

## Test your solution

Write your code in [exercise.py](./exercise.py), then run the tests from this folder:

```bash
cd 06-reverse-text
python3 -m unittest -v
```

## Hints

Try for a while before you open these. Each one gives away a little more.

<details>
<summary>Hint 1</summary>

With a loop, put each character in **front** of what you have so far: `result = char + result`.

</details>

<details>
<summary>Hint 2</summary>

The slicing version is `text[::-1]`: a slice of the whole string, stepping backwards.

</details>

<details>
<summary>Hint 3</summary>

For words: `sentence.split()` gives a list of words (and ignores extra spaces), and `" ".join(words)` puts a list back together. Reverse the list in between.

</details>

## Take it further

Write `is_reversible_word(word)`, which checks a word against a list of words and says whether its reverse is a real word too, like `stressed` and `desserts`.

A full solution is in [solutions/06-reverse-text.py](../solutions/06-reverse-text.py).

Next: [7. Count vowels](../07-count-vowels/)
