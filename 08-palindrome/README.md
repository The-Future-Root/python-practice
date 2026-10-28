# 8. Palindrome check

**Level:** Easy. **You'll practise:** cleaning strings, comparing with a reversed copy.

A **palindrome** reads the same forwards and backwards: `racecar`, `level`, `noon`. Whole sentences can be palindromes too, once you ignore spaces, punctuation and capital letters: "A man, a plan, a canal: Panama!"

Write `is_palindrome(text)`, which returns `True` if the text is a palindrome and `False` if it isn't. Ignore case, and ignore every character that isn't a letter or a digit.

## Examples

```python
>>> is_palindrome('racecar')
True
>>> is_palindrome('Racecar')
True
>>> is_palindrome('A man, a plan, a canal: Panama!')
True
>>> is_palindrome('hello')
False
```

## Rules

- Return a bool.
- An empty string, or one with no letters or digits, counts as a palindrome.

## Test your solution

Write your code in [exercise.py](./exercise.py), then run the tests from this folder:

```bash
cd 08-palindrome
python3 -m unittest -v
```

## Hints

Try for a while before you open these. Each one gives away a little more.

<details>
<summary>Hint 1</summary>

Build a cleaned-up version first: only the letters and digits, all lowercase.

</details>

<details>
<summary>Hint 2</summary>

`char.isalnum()` is `True` for letters and digits. Loop over the text and keep only those characters, lowercased.

</details>

<details>
<summary>Hint 3</summary>

Once you have `cleaned`, the check is one line: `return cleaned == cleaned[::-1]`.

</details>

## Take it further

Write `longest_palindrome(words)`, which takes a list of words and returns the longest one that's a palindrome.

A full solution is in [solutions/08-palindrome.py](../solutions/08-palindrome.py).

Next: [9. Word counter](../09-word-counter/)
