# Define an empty list to store tasks
todo_list = []

# Function to add a task to the list
def add_task(task):
    todo_list.append(task)
    print(f"Task '{task}' added to the to-do list.")

# Function to view all tasks
def view_tasks():
    if todo_list:
        print("To-Do List:")
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")
    else:
        print("Your to-do list is empty.")

# Function to remove a task by index
def remove_task(index):
    if 1 <= index <= len(todo_list):
        removed_task = todo_list.pop(index - 1)
        print(f"Task '{removed_task}' removed from the to-do list.")
    else:
        print("Invalid task index.")

# Main program loop
while True:
    print("\nTo-Do List Manager")
    print("Options:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Quit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        task = input("Enter the task: ")
        add_task(task)
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        view_tasks()
        index = int(input("Enter the index of the task to remove: "))
        remove_task(index)
    elif choice == '4':
        print("Thank you for using the to-do list manager. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")
