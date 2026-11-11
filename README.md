# Todo List

A simple command-line todo app written in Python.

## Features

- Add a task (with an optional priority)
- Show all tasks
- Mark a task as done
- Delete a task

## Project structure

- `models.py`: the `Task` class
- `services.py`: functions that work on the list of tasks
- `main-s2.py`: the menu (run this file)
- `test_models.py`, `test_services.py`: pytest tests

## How to run

```
py main-s2.py
```

## How to run tests

Install pytest first (once):

```
py -m pip install pytest
```

Then run:

```
py -m pytest -v
```