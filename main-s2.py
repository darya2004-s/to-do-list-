from services import add_task, complete_task, delete_task


def show_menu():
    print("1. Add task")
    print("2. Show tasks")
    print("3. Complete task")
    print("4. Delete task")
    print("5. Exit")
    
def ask_priority():
    text = input("Priority (default 1): ")
    if text == "":
        return 1
    try:
        return int(text)
    except ValueError:
        return None


def handle_add(tasks):
    title = input("Title: ")
    priority = ask_priority()
    if priority is None:
        print("Priority must be a number")
        return
    task = add_task(tasks, title, priority)
    print("Added:", task)
    
def handle_show(tasks):
    if len(tasks) == 0:
        print("No tasks")
    else:
        for task in tasks:
            print(task)
def handle_delete(tasks):
    title = input("Title: ")
    if delete_task(tasks, title):
        print("Deleted")
    else:
        print("Task not found")
def handele_complete(tasks):
    title = input("Title: ")
    if complete_task(tasks, title):
        print("Done")
    else:
        print("Task not found")
     

def main():
    tasks = []
    while True:
        show_menu()
        choice = input("Choose: ")

        if choice == "1":
            handle_add(tasks)

        elif choice == "2":
            handle_show(tasks)

        elif choice == "3":
            handele_complete(tasks)


        elif choice == "4":
            handle_delete(tasks)

        elif choice == "5":
            print("Bye")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()