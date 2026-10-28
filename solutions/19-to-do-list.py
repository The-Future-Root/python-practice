# Solution to 19. To-do list

import json


def add_task(tasks, text):
    """Add a task (with surrounding spaces stripped) to the end of the list."""
    tasks.append(text.strip())


def complete_task(tasks, number_text):
    """Remove task number `number_text` (counting from 1) and return its text, or return None."""
    try:
        number = int(number_text)
    except ValueError:
        return None
    if 1 <= number <= len(tasks):
        return tasks.pop(number - 1)
    return None


def format_tasks(tasks):
    """Return a list of lines like "1. Buy coffee beans", or ["No tasks"] if there are none."""
    if not tasks:
        return ["No tasks"]
    return [f"{number}. {task}" for number, task in enumerate(tasks, start=1)]


def load_tasks(path):
    """Return the list of tasks saved at path, or an empty list if the file doesn't exist."""
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def save_tasks(tasks, path):
    """Save the list of tasks to path as JSON."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2, ensure_ascii=False)


def main(path="tasks.json"):
    """Load the tasks, then read commands until "quit"."""
    tasks = load_tasks(path)
    while True:
        line = input("> ").strip()
        if not line:
            continue
        parts = line.split(maxsplit=1)
        command = parts[0].lower()
        if command == "add":
            if len(parts) < 2:
                print("Usage: add <task>")
                continue
            add_task(tasks, parts[1])
            print(f"Added: {tasks[-1]}")
        elif command == "done":
            number_text = parts[1] if len(parts) > 1 else ""
            task = complete_task(tasks, number_text)
            if task is None:
                print(f"No task number {number_text}")
            else:
                print(f"Done: {task}")
        elif command == "list":
            for line in format_tasks(tasks):
                print(line)
        elif command == "quit":
            save_tasks(tasks, path)
            print("Goodbye!")
            break
        else:
            print("Unknown command")


if __name__ == "__main__":
    main()
