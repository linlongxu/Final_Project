# Command Line Task Manager

## Overview
This is a Python-based **Command Line Task Manager** that allows users to:
- Add, list, query, mark as complete, delete, and report tasks.
- Store tasks persistently using a hidden `.todo.pickle` file in the user's home directory.
- Manage tasks entirely from the command line without the need for a graphical interface.

## Features
1. **Add Tasks**: Create tasks with optional due dates and priorities.
2. **List Tasks**: Display tasks that are not yet completed, sorted by due date and priority.
3. **Query Tasks**: Search for tasks based on specific keywords.
4. **Mark Tasks as Complete**: Mark tasks as completed while keeping them for reporting.
5. **Delete Tasks**: Permanently remove tasks from the list.
6. **Report**: Display all tasks, including completed and pending tasks.
7. **Persistent Storage**: Tasks are saved in a `.todo.pickle` file.


## Requirements
- Modules:
  - `argparse`
  - `pickle`
  - `os`
  - `datetime`
