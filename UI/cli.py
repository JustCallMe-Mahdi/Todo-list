from Todo.services.task_manager import TaskManager
from Todo.infra.storage import Storage

def main():
    storage = Storage("tasks.json")
    manager = TaskManager()
    manager.tasks = storage.load()
    manager._id_counter = max([t.id for t in manager.tasks], default=0) + 1

    while True:
        print("\n1. List Tasks\n2. Add Task\n3. Complete Task\n4. Remove Task\n5. Exit")
        choice = input("Choose: ")

        if choice == "1":
            for task in manager.list_tasks():
                status = "✅" if task.done else "❌"
                print(f"{task.id}: {task.title} {status}")
        elif choice == "2":
            title = input("Task title: ")
            manager.add_task(title)
            storage.save(manager.tasks)
        elif choice == "3":
            task_id = int(input("Task ID to complete: "))
            if manager.complete_task(task_id):
                storage.save(manager.tasks)
        elif choice == "4":
            task_id = int(input("Task ID to remove: "))
            if manager.remove_task(task_id):
                storage.save(manager.tasks)
        elif choice == "5":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
