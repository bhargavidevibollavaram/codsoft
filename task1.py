tasks = {}

while True:
    print("1. Add task")
    print("2. View tasks")
    print("3. Quit")
    choice = input("Choose an option: ")
    
    if choice == "1":
        task_name = input("Enter task name: ")
        task_description = input("Enter task description: ")
        tasks[task_name] = task_description
    elif choice == "2":
        print("Tasks:")
        for task_name, task_description in tasks.items():
            print(f"{task_name}: {task_description}")
    elif choice == "3":
        break
    else:
        print("Invalid choice!")

