tasks = []

while True:
    print("\n===== TO DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks") 
    print("3. Delete Task")
    print("4. Search Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to delete.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
            try:
                task_num = int(input("Enter task number to delete: "))
                if 1 <= task_num <= len(tasks):
                    removed = tasks.pop(task_num - 1)
                    print(f"Task '{removed}' deleted successfully!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == "4":
        if len(tasks) == 0:
            print("No tasks to search.")
        else:
            keyword = input("Enter keyword to search: ").lower()
            found = []
            for i, task in enumerate(tasks, start=1):
                if keyword in task.lower():
                    found.append(f"{i}. {task}")
            
            if found:
                print("\nSearch Results:")
                for result in found:
                    print(result)
            else:
                print("No matching tasks found.")

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice. Try again.")
