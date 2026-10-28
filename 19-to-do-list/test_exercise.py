import json
import pathlib
import subprocess
import sys
import tempfile
import unittest

from exercise import add_task, complete_task, format_tasks, load_tasks, save_tasks

PROGRAM = pathlib.Path(__file__).with_name("exercise.py")


class TestFunctions(unittest.TestCase):
    def test_add(self):
        tasks = []
        add_task(tasks, "  Buy coffee beans ")
        self.assertEqual(tasks, ["Buy coffee beans"])

    def test_complete(self):
        tasks = ["A", "B", "C"]
        self.assertEqual(complete_task(tasks, "2"), "B")
        self.assertEqual(tasks, ["A", "C"])

    def test_complete_invalid(self):
        tasks = ["A"]
        for text in ("0", "2", "-1", "one", ""):
            self.assertIsNone(complete_task(tasks, text))
        self.assertEqual(tasks, ["A"])

    def test_format(self):
        self.assertEqual(format_tasks(["Buy beans", "Call landlord"]), ["1. Buy beans", "2. Call landlord"])
        self.assertEqual(format_tasks([]), ["No tasks"])

    def test_save_and_load(self):
        with tempfile.TemporaryDirectory() as folder:
            path = pathlib.Path(folder) / "tasks.json"
            self.assertEqual(load_tasks(path), [])
            save_tasks(["One", "Two"], path)
            self.assertEqual(json.loads(path.read_text(encoding="utf-8")), ["One", "Two"])
            self.assertEqual(load_tasks(path), ["One", "Two"])


class TestProgram(unittest.TestCase):
    def setUp(self):
        self.folder = tempfile.TemporaryDirectory()

    def tearDown(self):
        self.folder.cleanup()

    def run_program(self, *commands):
        result = subprocess.run([sys.executable, str(PROGRAM)], input="\n".join(commands) + "\n",
                                capture_output=True, text=True, timeout=10, cwd=self.folder.name)
        return result.stdout + result.stderr

    def test_session(self):
        output = self.run_program("add Buy coffee beans", "add Call the landlord", "list", "done 1", "done 9",
                                  "list", "quit")
        for line in ("Added: Buy coffee beans", "1. Buy coffee beans", "2. Call the landlord",
                     "Done: Buy coffee beans", "No task number 9", "1. Call the landlord", "Goodbye!"):
            self.assertIn(line, output)

    def test_remembers(self):
        self.run_program("add Water the plants", "quit")
        self.assertIn("1. Water the plants", self.run_program("list", "quit"))

    def test_mistakes(self):
        output = self.run_program("add", "dance", "done", "list", "quit")
        self.assertIn("Usage: add <task>", output)
        self.assertIn("Unknown command", output)
        self.assertIn("No tasks", output)


if __name__ == "__main__":
    unittest.main()
