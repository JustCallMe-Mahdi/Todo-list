from Todo.core.entities import Task


class TaskManager:
    def __init__(self):
        self.tasks: list[Task] = []
        self._id_counter = 1

    def add_task(self, title: str) -> Task:
        task = Task(id=self._id_counter, title=title)
        self.tasks.append(task)
        self._id_counter += 1
        return task

    def complete_task(self, task_id: int) -> bool:
        for task in self.tasks:
            if task.id == task_id:
                task.done = True
                return True
        return False

    def list_tasks(self) -> list[Task]:
        return self.tasks

    def remove_task(self, task_id: int) -> None:
        for task in self.tasks:
            if task.id == task_id:
                self.tasks.remove(task)
                return True
        return False
