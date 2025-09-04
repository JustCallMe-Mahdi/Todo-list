from dataclasses import dataclass
from datetime import datetime

@dataclass
class Task:
    id: int
    title: str
    done: bool = False
    created_at: datetime = datetime.now()