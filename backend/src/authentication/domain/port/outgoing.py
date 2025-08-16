import abc

from authentication.domain.model.user import User


class UserRepository(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def add_user(self, vote: User) -> User:
        raise NotImplementedError

    @abc.abstractmethod
    def find(self, username: str) -> User:
        raise NotImplementedError


class UserNotFoundError(Exception):
    """Exception raised when no user found in repository"""


class UserAlreadyExistsError(Exception):
    """Exception raised when no user found in repository"""
