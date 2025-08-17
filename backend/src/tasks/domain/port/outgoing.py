import abc
from typing import List

from tasks.domain.model.task import Task


class TaskRepository(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def add_new_task(self, task: Task) -> Task:
        raise NotImplementedError

    @abc.abstractmethod
    def gel_all_tasks(self) -> List[Task]:
        raise NotImplementedError

    @abc.abstractmethod
    def update_task(self, task: Task) -> Task:
        raise NotImplementedError

    @abc.abstractmethod
    def remove_task(self, task_id: str):
        raise NotImplementedError


class TaskNotFoundError(Exception):
    """Exception raised when a task is not found."""
