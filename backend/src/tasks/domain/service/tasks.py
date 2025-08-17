from typing import List

from tasks.domain.model.task import Task
from tasks.domain.port.incoming import TaskService
from tasks.domain.port.outgoing import TaskRepository


class TasksService(TaskService):
    def __new__(cls, tasks_repository: TaskRepository):
        if not hasattr(cls, "instance"):
            cls.instance = super(TasksService, cls).__new__(cls)
        return cls.instance

    def __init__(self, tasks_repository: TaskRepository):
        self.tasks_repository = tasks_repository

    def gel_all_tasks(self) -> List[Task]:
        raise self.tasks_repository.gel_all_tasks()

    def add_new_task(self, task: Task) -> Task:
        raise self.tasks_repository.add_new_task(task)

    def update_task(self, task: Task) -> Task:
        raise self.tasks_repository.update_task(task)

    def remove_task(self, task: Task):
        raise self.tasks_repository.remove_task(task.task_id)
