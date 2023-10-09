import json

class Task:
    def __init__(self, title, description, status="Incomplete"):
        self.title = title
        self.description = description
        self.status = status

    def __str__(self):
        return f"{self.title} - {self.description} ({self.status})"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def delete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            del self.tasks[task_index]
            return True
        return False

    def view_tasks(self):
        if not self.tasks:
            print("Your to-do list is empty.")
        else:
            for i, task in enumerate(self.tasks):
                print(f"{i + 1}. {task}")

    def save_tasks(self, filename):
        with open(filename, 'w') as file:
            task_list = [vars(task) for task in self.tasks]
            json.dump(task_list, file)

    def load_tasks(self, filename):
        try:
            with open(filename, 'r') as file:
                task_list = json.load(file)
                self.tasks = [Task(**task) for task in task_list]
        except FileNotFoundError:
            print("File not found.")
        except json.JSONDecodeError:
            print("Invalid JSON format.")

def main():
    todo_list = ToDoList()

    while True:
        print("\nTodo List Menu:")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. View Tasks")
        print("4. Save Tasks to File")
        print("5. Load Tasks from File")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            task = Task(title, description)
            todo_list.add_task(task)
            print("Task added successfully!")

        elif choice == '2':
            todo_list.view_tasks()
            task_index = int(input("Enter the index of the task to delete: ")) - 1
            if todo_list.delete_task(task_index):
                print("Task deleted successfully!")
            else:
                print("Invalid task index.")

        elif choice == '3':
            todo_list.view_tasks()

        elif choice == '4':
            filename = input("Enter the filename to save tasks: ")
            todo_list.save_tasks(filename)
            print(f"Tasks saved to {filename}.")

        elif choice == '5':
            filename = input("Enter the filename to load tasks: ")
            todo_list.load_tasks(filename)
            print(f"Tasks loaded from {filename}.")

        elif choice == '6':
            print("Exiting the Todo List app.")
            break

        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
