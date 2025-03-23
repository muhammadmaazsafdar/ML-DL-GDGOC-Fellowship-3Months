def read_tasks():
    try:
        with open('tasks.txt', 'r') as file:
            tasks = file.readlines()
        return [task.strip() for task in tasks]
    except FileNotFoundError:
        with open('tasks.txt', 'w') as file:
            pass
        return []

def write_tasks(tasks):
    with open('tasks.txt', 'w') as file:
        for task in tasks:
            file.write(task + '\n')

def view_tasks():
    tasks = read_tasks()
    if not tasks:
        print("\nNo tasks found.\n")
    else:
        print("\n--- Task List ---")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")
        print()


def add_task(task):
    tasks = read_tasks()
    tasks.append(task)
    write_tasks(tasks)
    print("\nTask added successfully.\n")


def remove_task(task_number):
    tasks = read_tasks()
    try:
        removed = tasks.pop(task_number - 1)
        write_tasks(tasks)
        print(f"\nTask '{removed}' removed successfully.\n")
    except IndexError:
        print("\nInvalid task number.\n")


def update_task(task_number, new_task):
    tasks = read_tasks()
    try:
        tasks[task_number - 1] = new_task
        write_tasks(tasks)
        print("\nTask updated successfully.\n")
    except IndexError:
        print("\nInvalid task number.\n")


# User Interface - CLI Menu
def menu():
    while True:
        print("\n=== Task Manager ===")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Update Task")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice (1-5): "))
        except ValueError:
            print("\nPlease enter a valid number.\n")
            continue

        if choice == 1:
            view_tasks()
        elif choice == 2:
            task = input("Enter the new task: ")
            add_task(task)
        elif choice == 3:
            try:
                task_num = int(input("Enter the task number to remove: "))
                remove_task(task_num)
            except ValueError:
                print("\nPlease enter a valid number.\n")
        elif choice == 4:
            try:
                task_num = int(input("Enter the task number to update: "))
                new_task = input("Enter the updated task: ")
                update_task(task_num, new_task)
            except ValueError:
                print("\nPlease enter a valid number.\n")
        elif choice == 5:
            print("\nExiting Task Manager. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please select from 1 to 5.\n")


if __name__ == "__main__":
    menu()
