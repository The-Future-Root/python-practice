# 19. To-do list
#
# The problem, examples and rules are in README.md.
# Test with:  python3 -m unittest -v

import json


def add_task(tasks, text):
    """Add a task (with surrounding spaces stripped) to the end of the list."""
    pass


def complete_task(tasks, number_text):
    """Remove task number `number_text` (counting from 1) and return its text, or return None."""
    pass


def format_tasks(tasks):
    """Return a list of lines like "1. Buy coffee beans", or ["No tasks"] if there are none."""
    pass


def load_tasks(path):
    """Return the list of tasks saved at path, or an empty list if the file doesn't exist."""
    pass


def save_tasks(tasks, path):
    """Save the list of tasks to path as JSON."""
    pass


def main(path="tasks.json"):
    """Load the tasks, then read commands until "quit"."""
    pass


if __name__ == "__main__":
    main()
