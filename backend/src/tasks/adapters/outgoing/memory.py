import uuid
from typing import List

from tasks.domain.model.task import Task
from tasks.domain.port.outgoing import TaskNotFoundError, TaskRepository


class InMemoryTaskRepository(TaskRepository):
    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(InMemoryTaskRepository, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.tasks = []

    def add_new_task(self, task: Task) -> Task:
        task.task_id = str(uuid.uuid4())
        self.tasks.append(task)
        return task

    def gel_all_tasks(self) -> List[Task]:
        return self.tasks

    def update_task(self, task: Task) -> Task:
        task_to_update = self._find(task.task_id)
        task_to_update.name = task.name
        task_to_update.is_done = task.is_done
        return task_to_update

    def remove_task(self, task_id: str):
        self.tasks.remove(Task(task_id))

    def _find(self, task_id: str) -> Task:
        try:
            return next(x for x in self.tasks if x.task_id == task_id)
        except StopIteration:
            raise TaskNotFoundError()
