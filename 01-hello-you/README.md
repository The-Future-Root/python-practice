# 1. Hello, you

**Level:** Easy. **You'll practise:** `input()`, string methods, f-strings.

Write a program that asks for a person's first name and last name, then greets them.

People type names in all sorts of ways: `alex`, `ALEX`, `  Alex  `. Tidy each name before you use it, so the greeting always looks right: no spaces at the ends, and a capital letter at the start of each word.

## Example

What the user typed is shown after each prompt:

```
First name:   alex
Last name: KIM  
Hello, Alex Kim! Nice to meet you.
```

## Rules

- Ask `First name: ` first, then `Last name: `.
- Print exactly `Hello, Alex Kim! Nice to meet you.`, using the tidied names.

## Test your solution

Write your code in [exercise.py](./exercise.py), then run the tests from this folder:

```bash
cd 01-hello-you
python3 -m unittest -v
```

## Hints

Try for a while before you open these. Each one gives away a little more.

<details>
<summary>Hint 1</summary>

You need two `input()` calls and one `print()`.

</details>

<details>
<summary>Hint 2</summary>

`.strip()` removes spaces at both ends, and `.title()` capitalises each word. You can chain them: `name.strip().title()`.

</details>

<details>
<summary>Hint 3</summary>

`print(f"Hello, {first} {last}! Nice to meet you.")`

</details>

## Take it further

Ask for a middle name too, and leave it out of the greeting if the user just presses Enter.

A full solution is in [solutions/01-hello-you.py](../solutions/01-hello-you.py).

Next: [2. Simple calculator](../02-simple-calculator/)
