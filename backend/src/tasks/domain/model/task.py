from dataclasses import dataclass


@dataclass
class Task:
    task_id: str
    name: str
    is_done: str

    def __init__(self, task_id: str):
        self.task_id = task_id

    def __eq__(self, other):
        return self.task_id == other.task_id

    def __hash__(self):
        return hash(self.task_id)
