from models import Task


def test_task_starts_not_done():
    task = Task("shop")
    assert task.done is False


def test_task_complete():
    task = Task("shop")
    task.complete()
    assert task.done is True
    
def test_task_default_priority():
    task = Task("shop")
    assert task.priority == 1


def test_task_str_not_done():
    task = Task("shop", 2)
    assert str(task) == "[ ] shop (priority: 2)"
    
def test_task_str_done():
    task = Task("shop", 1)
    assert str(task) == "[ ] shop (priority: 1)"
    