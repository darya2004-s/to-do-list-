class Task:
    def __init__(self, title, priority=1):
        self.title = title
        self.done = False
        self.priority = priority

    def complete(self):
        self.done = True
        
    def find_task(tasks, title):
        for task in tasks:
            if task.title == title:
                return task
        return None

    def __str__(self):
        mark = "✓" if self.done else " "
        return f"[{mark}] {self.title} (priority: {self.priority})"
    