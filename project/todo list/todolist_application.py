class ToDoList:
    def __init__(self):
        self.tasks = []

    def display_menu(self):
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Exit")

    def add_task(self):
        task_name = input("Enter the task name: ")
        self.tasks.append({"name": task_name, "completed": False})
        print("Task added successfully!")

    def view_tasks(self):
        print("\nTask List:")
        for index, task in enumerate(self.tasks, start=1):
            status = "Completed" if task["completed"] else "Not Completed"
            print(f"{index}. {task['name']} - {status}")

    def run(self):
        while True:
            self.display_menu()
            try:
                choice = int(input("Enter your choice (1-3): "))
                if choice == 1:
                    self.add_task()
                elif choice == 2:
                    self.view_tasks()
                elif choice == 3:
                    print("Exiting the To-Do List application. Goodbye!")
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 and 3.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    todo_list = ToDoList()
    todo_list.run()
