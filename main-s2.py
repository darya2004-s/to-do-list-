from services import add_task, complete_task, delete_task


def show_menu():
    print("1. Add task")
    print("2. Show tasks")
    print("3. Complete task")
    print("4. Delete task")
    print("5. Exit")


def main():
    tasks = []
    while True:
        show_menu()
        choice = input("Choose: ")

        if choice == "1":
            title = input("Title: ")
            priority_text = input("Priority (default 1): ")
            if priority_text == "":
                priority = 1
            else:
                try:
                    priority = int(priority_text)
                except ValueError:
                    print("Priority must be a number")
                    continue
            task = add_task(tasks, title, priority)
            print("Added:", task)

        elif choice == "2":
            if len(tasks) == 0:
                print("No tasks")
            else:
                for task in tasks:
                    print(task)

        elif choice == "3":
            title = input("Title: ")
            if complete_task(tasks, title):
                print("Done")
            else:
                print("Task not found")

        elif choice == "4":
            title = input("Title: ")
            if delete_task(tasks, title):
                print("Deleted")
            else:
                print("Task not found")

        elif choice == "5":
            print("Bye")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()