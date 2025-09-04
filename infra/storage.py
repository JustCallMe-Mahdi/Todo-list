import json
from Todo.core.entities import Task
from datetime import datetime

class Storage:
    def __init__(self, filename: str):
        self.filename = filename

    def save(self, tasks: list[Task]) -> None:
        data = [
            {
                "id": task.id,
                "title": task.title,
                "done": task.done,
                "created_at": task.created_at.isoformat()
            }
            for task in tasks
        ]
        with open(self.filename, "w") as f:
            json.dump(data, f, indent=2)

    def load(self) -> list[Task]:
        try:
            with open(self.filename, "r") as f:
                data = json.load(f)
                return [
                    Task(
                        id=item["id"],
                        title=item["title"],
                        done=item["done"],
                        created_at=datetime.fromisoformat(item["created_at"])
                    )
                    for item in data
                ]
        except FileNotFoundError:
            return []
