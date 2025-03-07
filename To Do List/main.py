File = "task.txt"
def task_adding(task):
    with open(File, "a") as file:
        file.write(task + "\n")
        print(f"Task '{task}' added successfully.")
def task_view(task):
    with open(File, "r") as file:
        tasks = file.readlines()
        if tasks:
            print("Tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task.strip()}")
        else:
            print("No tasks available.")



def task_deletion(task_number):
    with open(File, "r") as file:
        tasks = file.readlines()
        if 1 <= task_number <= len(tasks):
            deleted_task = tasks.pop(task_number - 1)
            with open(File, "w") as file:
                file.writelines(tasks)
                print(f"\nTask '{deleted_task.strip()}' deleted successfully.")
        else:
            print("\nInvalid task number.")




def task_editing(task_number, new_task):
    with open(File, "r") as file:
        tasks = file.readlines()
        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1] = new_task + "\n"
            with open(File, "w") as file:
                file.writelines(tasks)  
                print(f"\nTask updated successfully to: '{new_task}'\n")
        else:
             print("\nInvalid task number.")




while True:
    print("\nTo-Do List Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Edit Task")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        task = input("Enter a new task: ")
        task_adding(task)

    elif choice == "2":
        task_view()

    elif choice == "3":
        task_view()
        task_num = int(input("\nEnter the task number to delete: "))
        task_deletion(task_num)

    elif choice == "4":
        task_view()
        task_num = int(input("\nEnter the task number to edit: "))
        new_task = input("Enter the new task: ")
        task_editing(task_num, new_task)

    elif choice == "5":
        print("\nExiting the application.")
        break 

    else:
        print("\nInvalid choice. Please enter a number between 1 and 5.")