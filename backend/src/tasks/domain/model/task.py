from dataclasses import dataclass

from pydantic import BaseModel, Field


@dataclass
class Task(BaseModel):
    name: str
    is_done: bool
    task_id: str = Field(default=None, title="Task ID")

    def __eq__(self, other):
        return self.task_id == other.task_id

    def __hash__(self):
        return hash(self.task_id)
