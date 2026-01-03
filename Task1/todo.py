import os

FILENAME = "tasks.txt"

# Load tasks from file
def load_tasks():
    tasks = []
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            for line in file:
                task, status = line.strip().split("|")
                tasks.append({"task": task, "status": status})
    return tasks

# Save tasks to file
def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        for t in tasks:
            file.write(f"{t['task']}|{t['status']}\n")

# Display tasks
def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks found.")
        return

    print("\nYour To-Do List:")
    for i, t in enumerate(tasks, start=1):
        print(f"{i}. {t['task']} - {t['status']}")

# Add task
def add_task(tasks):
    task_name = input("\nEnter task name: ")
    tasks.append({"task": task_name, "status": "Pending"})
    save_tasks(tasks)
    print("Task added successfully!")

# Update task
def update_task(tasks):
    view_tasks(tasks)
    try:
        index = int(input("\nEnter task number to update: ")) - 1
        if 0 <= index < len(tasks):
            new_name = input("Enter new task name: ")
            tasks[index]["task"] = new_name
            save_tasks(tasks)
            print("Task updated successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Mark task as completed
def complete_task(tasks):
    view_tasks(tasks)
    try:
        index = int(input("\nEnter task number to mark completed: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["status"] = "Completed"
            save_tasks(tasks)
            print("Task marked as completed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Delete task
def delete_task(tasks):
    view_tasks(tasks)
    try:
        index = int(input("\nEnter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            tasks.pop(index)
            save_tasks(tasks)
            print("Task deleted successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Main menu
def main():
    tasks = load_tasks()

    while True:
        print("\n--- TO-DO LIST MENU ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Mark Task as Completed")
        print("5. Delete Task")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            update_task(tasks)
        elif choice == "4":
            complete_task(tasks)
        elif choice == "5":
            delete_task(tasks)
        elif choice == "6":
            print("Exiting To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
