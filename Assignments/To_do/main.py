from todo import Todo_Item, Todo_List
import os

def save_todo_list(todo_list):
    directory = r"C:\Users\91800\OneDrive\Desktop\asrithA\suretrust\suretrust python\KAMISETTY-SATHVIKA-g32-python\Assignments\To_do\todo_data"
    
    with open(f"{directory}/{todo_list.owner.lower()}.txt", "w") as f:
        lines = []

        for item in todo_list.todo_items:
            priority = item.priority if item.priority else "None"
            done = "True" if item.done else "False"
            task = item.task.replace(",", " ")
            line = ",".join([priority, done, task])
            lines.append(line)

        f.write("\n".join(lines))

print("Welcome to TODO APP")
directory = r"C:\Users\91800\OneDrive\Desktop\asrithA\suretrust\suretrust python\KAMISETTY-SATHVIKA-g32-python\Assignments\To_do\todo_data"

while True:
    owner_name = input("Hello, Please enter your name: ")
    if owner_name:
        break
    else:
        print("Owner Name can't be empty...")

PATH = f"{directory}/{owner_name.lower()}.txt"

try:
    with open(PATH, "x") as f:
        print(f"Welcome {owner_name} to our TODO app")
        user_list = Todo_List(owner_name)
except FileExistsError:
    print(f"Welcome Back")
    with open(PATH, "r") as f:
        todo_data = f.readlines()
        todo_items = []
        for line in todo_data:
            line = line.strip()
            priority, done, task = line.split(",")
            done = True if done == "True" else False
            priority = None if priority == "None" else priority
            todo_item = Todo_Item(task, priority, done)
            todo_items.append(todo_item)
        user_list = Todo_List(owner_name, todo_items)

while True:
    print("""\n\nWhat do you want to do?
    
    1. Create a new task
    2. View existing tasks
    3. Mark a task as done
    4. Edit an old task 
    5. Delete a task
    6. Exit
    """)

    while True:
        choice = input("Enter a number (1-6): ")
        try:
            choice = int(choice)
            if 1 <= choice <= 6:
                break
            else:
                print("Choice must be between 1-6")
        except ValueError:
            print("Choice must be a valid number")

    if choice == 6:
        save_todo_list(user_list)
        print("Your tasks have been saved. Goodbye!")
        break

    elif choice == 1:
        task = input("\nTask: ").strip()
        while not task:
            print("Task must not be empty!")
            task = input("\nTask: ").strip()

        priority = input("\nPriority (High, Medium, Low): ").strip().title()
        while priority and priority not in ["High", "Medium", "Low"]:
            print("Priority must be one of", ["High", "Medium", "Low"])
            priority = input("\nPriority (High, Medium, Low): ").strip().title()

        done = input("\nDone? (y/N): ").strip().lower()
        done = True if done in ["y", "yes"] else False

        created_item = Todo_Item(task, priority or None, done)
        print("\nNew task created")
        print(created_item)

        user_list.add_todo_item(created_item)
        save_todo_list(user_list)

    elif choice == 2:
        print("\nYour To-Do List:")
        print(user_list)

    elif choice == 3:
        task_number = int(input("Enter the task number to mark as done: "))
        if 0 <= task_number < len(user_list.todo_items):
            user_list.todo_items[task_number].finish()
            print(f"Task {task_number} marked as done.")
            save_todo_list(user_list)
        else:
            print("Invalid task number")

    elif choice == 4:
        task_number = int(input("Enter the task number to edit: "))
        if 0 <= task_number < len(user_list.todo_items):
            task = input("\nNew Task Description: ").strip()
            while not task:
                print("Task must not be empty!")
                task = input("\nNew Task Description: ").strip()

            priority = input("\nNew Priority (High, Medium, Low): ").strip().title()
            while priority and priority not in ["High", "Medium", "Low"]:
                print("Priority must be one of", ["High", "Medium", "Low"])
                priority = input("\nNew Priority (High, Medium, Low): ").strip().title()
            done = input("\nDone? (y/N): ").strip().lower()
            done = True if done in ["y", "yes"] else False
            user_list.todo_items[task_number] = Todo_Item(task, priority or None, done)
            print(f"Task {task_number} has been edited.")
            save_todo_list(user_list)
        else:
            print("Invalid task number")

    elif choice == 5:
        task_number = int(input("Enter the task number to delete: "))
        if 0 <= task_number < len(user_list.todo_items):
            del user_list.todo_items[task_number]
            print(f"Task {task_number} has been deleted.")
            save_todo_list(user_list)
        else:
            print("Invalid task number")

    else:
        print(f"Invalid choice: {choice}")
