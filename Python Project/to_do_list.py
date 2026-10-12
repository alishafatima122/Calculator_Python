#===========================
# To-Do List Application
# language: Python
#===========================
tasks = []

try:
    with open("tasks.txt", "r") as file:
        for line in file:
            tasks.append(line.strip())

except FileNotFoundError:
    with open("tasks.txt", "w"):
        pass

def save_tasks():

    with open("tasks.txt", "w") as file:

        for task in tasks:
            file.write(task + "\n")

while True:

    print("\n===========================")
    print("       To-Do List")
    print("===========================")

    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Clear Tasks")
    print("5. Exit")


    choice = input("Enter your choice: ")


    if choice == '1':
        task = input("Enter the task: ")
        tasks.append(task)
        save_tasks()
        print(f"Task '{task}' added.")


    elif choice == '2':
        if not tasks:
            print("No tasks in the list.")
        else:
            print("\nTasks:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")


    elif choice == '3':
        if not tasks:
            print("No tasks to remove.")
        else:

            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")
            task_number = int(input("Enter task number to remove: "))

            if 1 <= task_number <= len(tasks):
                removed_task = tasks.pop(task_number - 1)
                save_tasks()
                print(f"Task '{removed_task}' removed.")
            else:
                print("Invalid task number.")


    elif choice == '4':
        tasks.clear()
        save_tasks()
        print("All tasks cleared.")


    elif choice == '5':
        print("Exiting the application.")
        break

    else:
        print("Invalid choice.")