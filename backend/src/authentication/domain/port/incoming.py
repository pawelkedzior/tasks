import abc

from authentication.domain.model.user import User


class AuthService(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def attempt_authentication(self, user: User) -> str:
        raise NotImplementedError

    @abc.abstractmethod
    def register_new_user(self, user: User):
        raise NotImplementedError
