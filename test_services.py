import pytest
from services import add_task, find_task, complete_task, delete_task, count_done


@pytest.fixture
def tasks():
    return []


def test_add_task_adds_to_list(tasks):
    add_task(tasks, "shop")
    assert len(tasks) == 1


def test_add_task_returns_task(tasks):
    task = add_task(tasks, "shop")
    assert task.title == "shop"


def test_find_task_found(tasks):
    add_task(tasks, "shop")
    result = find_task(tasks, "shop")
    assert result.title == "shop"


def test_find_task_not_found(tasks):
    result = find_task(tasks, "shop")
    assert result is None 
    
def test_complete_task_success(tasks):
    add_task(tasks, "shop")
    result = complete_task(tasks, "shop")
    assert result is True
    assert tasks[0].done is True
    
def test_complete_task_not_found(tasks):
    result = complete_task(tasks, "shop")
    assert result is False 
    
def test_delete_task_success(tasks):
    add_task(tasks, "shop")
    result = delete_task(tasks, "shop")
    assert result is True
    assert len(tasks) == 0
    
def test_delete_task_not_found (tasks):
    result=delete_task(tasks,"shop")
    assert result is False 
    
def test_count_done(tasks):
    add_task(tasks, "a")
    add_task(tasks, "b")
    complete_task(tasks, "a")
    assert count_done(tasks) == 1