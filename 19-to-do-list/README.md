# 19. To-do list

**Level:** Harder. **You'll practise:** a command loop, lists, error handling, saving to a file.

Build a small to-do list program that remembers your tasks between runs. It reads commands until you type `quit`:

| Command | What it does | It prints |
|---|---|---|
| `add <task>` | adds a task to the end of the list | `Added: Buy coffee beans` |
| `done <number>` | removes that task (numbers start at 1) | `Done: Buy coffee beans`, or `No task number 5` |
| `list` | shows the tasks, numbered from 1 | `1. Buy coffee beans`, or `No tasks` |
| `quit` | saves the tasks and stops | `Goodbye!` |

Anything else prints `Unknown command`. Tasks are saved to `tasks.json` in the folder you run the program from, so `list` shows them again next time.

As in the other problems, the real work goes in small functions that the tests can check, and `main()` runs the loop. Here's a session:

```
> add Buy coffee beans
Added: Buy coffee beans
> add Call the landlord
Added: Call the landlord
> list
1. Buy coffee beans
2. Call the landlord
> done 1
Done: Buy coffee beans
> done 9
No task number 9
> list
1. Call the landlord
> quit
Goodbye!
```

## Rules

- `add` with nothing after it prints `Usage: add <task>`.
- `done` with a number that's out of range or not a number prints `No task number ...`, and doesn't crash.

## Test your solution

Write your code in [exercise.py](./exercise.py), then run the tests from this folder:

```bash
cd 19-to-do-list
python3 -m unittest -v
```

## Hints

Try for a while before you open these. Each one gives away a little more.

<details>
<summary>Hint 1</summary>

`line.split(maxsplit=1)` splits a command into at most two parts: `"add Buy beans"` becomes `["add", "Buy beans"]`.

</details>

<details>
<summary>Hint 2</summary>

`complete_task` turns the text into a number inside `try`/`except ValueError`, checks it's between 1 and `len(tasks)`, and uses `tasks.pop(number - 1)`.

</details>

<details>
<summary>Hint 3</summary>

`load_tasks` catches `FileNotFoundError` and returns an empty list. `main` loads at the start and saves when you `quit`.

</details>

## Take it further

Mark tasks as done instead of deleting them, and show them with a tick: `1. [x] Buy coffee beans`. Then add a `clear` command that removes everything that's done.

A full solution is in [solutions/19-to-do-list.py](../solutions/19-to-do-list.py).

Next: [20. Grade report](../20-grade-report/)
