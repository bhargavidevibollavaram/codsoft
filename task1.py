


# To-Do List Program

tasks = []

def add_task():
    task = input("Enter the task: ")
    tasks.append(task)
    print("Task added!")

def view_tasks():
    print("To-Do List:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

def update_task():
    view_tasks()
    task_number = int(input("Enter task number to update: ")) - 1
    new_task = input("Enter new task: ")
    tasks[task_number] = new_task
    print("Task updated!")

def delete_task():
    view_tasks()
    task_number = int(input("Enter task number to delete: ")) - 1
    del tasks[task_number]
    print("Task deleted!")

while True:
    print("To-Do List App")
    print("1. Add task")
    print("2. View tasks")
    print("3. Update task")
    print("4. Delete task")
    print("5. Quit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        update_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        break
    else:
        print("Invalid choice entered!")