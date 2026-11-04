from models import Task


def add_task(tasks, title, priority=1):
    task = Task(title, priority)
    tasks.append(task)
    return task


def find_task(tasks, title):
    for task in tasks:
        if task.title == title:
            return task
    return None


def complete_task(tasks, title):
    task = find_task(tasks, title)
    if task is None:
        return False
    task.complete()
    return True


def delete_task(tasks, title):
    task = find_task(tasks, title)
    if task is None:
        return False
    tasks.remove(task)
    return True


def count_done(tasks):
    count = 0
    for task in tasks:
        if task.done:
            count += 1
    return count
