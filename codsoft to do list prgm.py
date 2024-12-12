class ToDoList:
    def __init__(self):
        self.tasks = {}

    def display_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            for task_id, task in self.tasks.items():
                status = "Completed" if task["completed"] else "Pending"
                print(f"{task_id}. {task['name']} - {status}")

    def add_task(self):
        task_name = input("Enter task name: ")
        task_id = len(self.tasks) + 1
        self.tasks[task_id] = {"name": task_name, "completed": False}
        print(f"Task '{task_name}' added successfully!")

    def update_task(self):
        self.display_tasks()
        task_id = int(input("Enter task ID to update: "))
        if task_id in self.tasks:
            task = self.tasks[task_id]
            print("1. Update task name")
            print("2. Mark task as completed")
            choice = input("Enter your choice: ")
            if choice == "1":
                task["name"] = input("Enter new task name: ")
                print("Task updated successfully!")
            elif choice == "2":
                task["completed"] = True
                print("Task marked as completed!")
            else:
                print("Invalid choice.")
        else:
            print("Task not found.")

    def delete_task(self):
        self.display_tasks()
        task_id = int(input("Enter task ID to delete: "))
        if task_id in self.tasks:
            del self.tasks[task_id]
            print("Task deleted successfully!")
        else:
            print("Task not found.")

def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List Menu:")
        print("1. Display tasks")
        print("2. Add task")
        print("3. Update task")
        print("4. Delete task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            todo_list.display_tasks()
        elif choice == "2":
            todo_list.add_task()
        elif choice == "3":
            todo_list.update_task()
        elif choice == "4":
            todo_list.delete_task()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()

