import json

def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks, task):
    tasks.append({"task": task, "completed": False})
    print(f"Added: {task}")

def update_task(tasks, index, new_task):
    try:
        tasks[index]["task"] = new_task
        print(f"Updated task {index} to: {new_task}")
    except IndexError:
        print("Invalid task index.")

def mark_completed(tasks, index):
    try:
        tasks[index]["completed"] = True
        print(f"Task {index} marked as completed.")
    except IndexError:
        print("Invalid task index.")

def delete_task(tasks, index):
    try:
        task = tasks.pop(index)
        print(f"Deleted task: {task['task']}")
    except IndexError:
        print("Invalid task index.")

def display_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return
    for i, task in enumerate(tasks):
        status = "✓" if task["completed"] else "✗"
        print(f"{i}. {task['task']} [{status}]")

if __name__ == "__main__":
    tasks = load_tasks()

    while True:
        print("\nTo-Do List:")
        display_tasks(tasks)
        print("\nOptions: 1. Add 2. Update 3. Complete 4. Delete 5. Exit")
        choice = int(input("Choose an option: "))

        if choice == 1:
            task = input("Enter task: ")
            add_task(tasks, task)
        elif choice == 2:
            index = int(input("Enter task number: "))
            new_task = input("Enter new task: ")
            update_task(tasks, index, new_task)
        elif choice == 3:
            index = int(input("Task to mark as complete: "))
            mark_completed(tasks, index)
        elif choice == 4:
            index = int(input("Task to delete: "))
            delete_task(tasks, index)
        elif choice == 5:
            save_tasks(tasks)
            print("Exiting...")
            break
        else:
            print("Invalid choice.")