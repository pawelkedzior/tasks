import abc
from typing import List

from tasks.domain.model.task import Task


class TaskService(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_all_tasks(self) -> List[Task]:
        raise NotImplementedError

    @abc.abstractmethod
    def add_new_task(self, task: Task) -> Task:
        raise NotImplementedError

    @abc.abstractmethod
    def update_task(self, task: Task) -> Task:
        raise NotImplementedError

    @abc.abstractmethod
    def remove_task(self, task: Task):
        raise NotImplementedError
