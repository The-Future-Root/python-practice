# 16. Caesar cipher

**Level:** Medium. **You'll practise:** `ord()` and `chr()`, the `%` operator, building strings.

The Caesar cipher is one of the oldest ways of hiding a message: shift every letter a fixed number of places along the alphabet. With a shift of 3, A becomes D, B becomes E, and at the end it wraps round, so X becomes A. Julius Caesar is said to have used it for military messages.

Write two functions:

- `encrypt(text, shift)` shifts every letter forward by `shift` places.
- `decrypt(text, shift)` undoes it.

Keep capitals as capitals and lowercase as lowercase, and leave everything that isn't a letter (spaces, digits, punctuation) unchanged.

## Examples

```python
>>> encrypt('hello', 3)
'khoor'
>>> encrypt('xyz', 3)
'abc'
>>> encrypt('Meet at 10pm!', 5)
'Rjjy fy 10ur!'
>>> decrypt('Rjjy fy 10ur!', 5)
'Meet at 10pm!'
```

## Rules

- Shifts can be bigger than 26, and can be negative.
- `decrypt(encrypt(text, n), n)` gives back the original text.

## Test your solution

Write your code in [exercise.py](./exercise.py), then run the tests from this folder:

```bash
cd 16-caesar-cipher
python3 -m unittest -v
```

## Hints

Try for a while before you open these. Each one gives away a little more.

<details>
<summary>Hint 1</summary>

Every character has a number: `ord("a")` is 97 and `chr(97)` is `"a"`. Work out each letter's position in the alphabet, 0 to 25, by subtracting the code for `"a"` (or `"A"` for capitals).

</details>

<details>
<summary>Hint 2</summary>

Add the shift and wrap round with `% 26`: `(position + shift) % 26`. Then turn it back into a letter by adding the base code again.

</details>

<details>
<summary>Hint 3</summary>

`decrypt` is just `encrypt` with the shift going backwards: `return encrypt(text, -shift)`.

</details>

## Take it further

The Caesar cipher is easy to break: there are only 26 possible shifts. Write `crack(text)`, which tries every shift and picks the one whose result contains the most common English words.

A full solution is in [solutions/16-caesar-cipher.py](../solutions/16-caesar-cipher.py).

Next: [17. Temperature converter](../17-temperature-converter/)
