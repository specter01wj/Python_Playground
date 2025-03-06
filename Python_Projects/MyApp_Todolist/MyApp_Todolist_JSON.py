import json
import os

TODO_FILE = "tasks.json"

def load_tasks():
    """Load tasks from a JSON file."""
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r") as file:
        return json.load(file)

def save_tasks(tasks):
    """Save tasks to a JSON file."""
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def show_tasks(tasks):
    """Display the to-do list with completion status."""
    if not tasks:
        print("No tasks found.")
        return
    for idx, task in enumerate(tasks, 1):
        status = "✅" if task["done"] else "❌"
        print(f"{idx}. {status} {task['task']}")

def add_task(tasks):
    """Add a new task."""
    task = input("Enter a new task: ")
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)
    print("Task added!")

def remove_task(tasks):
    """Remove a task."""
    show_tasks(tasks)
    try:
        index = int(input("Enter task number to remove: ")) - 1
        if 0 <= index < len(tasks):
            removed_task = tasks.pop(index)
            save_tasks(tasks)
            print(f"Removed task: {removed_task['task']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def mark_task_done(tasks):
    """Mark a task as completed."""
    show_tasks(tasks)
    try:
        index = int(input("Enter task number to mark as completed: ")) - 1
        if 0 <= index < len(tasks):
            if not tasks[index]["done"]:
                tasks[index]["done"] = True
                save_tasks(tasks)
                print("Task marked as completed!")
            else:
                print("Task is already completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    """Main program loop."""
    tasks = load_tasks()
    while True:
        print("\nTo-Do List:")
        show_tasks(tasks)
        print("\nOptions: [1] Add [2] Remove [3] Mark Completed [4] Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            remove_task(tasks)
        elif choice == "3":
            mark_task_done(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
