import os
import pickle
from datetime import datetime

class Task:
    """Representation of a task."""

    def __init__(self, name, priority=1, due_date=None):
        self.name = name
        self.priority = priority
        self.due_date = due_date
        self.created = datetime.now()
        self.completed = None

    def mark_complete(self):
        self.completed = datetime.now()

class Tasks:
    """A collection of Task objects."""

    def __init__(self):
        self.filepath = os.path.expanduser("~/.todo.pickle")
        if os.path.exists(self.filepath):
            with open(self.filepath, "rb") as file:
                self.tasks = pickle.load(file)
        else:
            self.tasks = []

    def pickle_tasks(self):
        """Save the tasks to a file."""
        with open(self.filepath, "wb") as file:
            pickle.dump(self.tasks, file)

    def add_task(self, name, priority=1, due_date=None):
        """Add a new task."""
        task = Task(name, priority, due_date)
        self.tasks.append(task)
        self.pickle_tasks()
        print(f"Task added: {task.name}")

    def list_tasks(self):
        """List all tasks."""
        for task in self.tasks:
            print(task.name)