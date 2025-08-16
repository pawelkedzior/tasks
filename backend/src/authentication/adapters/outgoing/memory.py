from authentication.domain.model.user import User
from authentication.domain.port.outgoing import (
    UserAlreadyExistsError,
    UserNotFoundError,
    UserRepository,
)


class InMemoryUserRepository(UserRepository):
    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(InMemoryUserRepository, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.users = []

    def add_user(self, user: User) -> User:
        try:
            self.find(user.username)
        except UserNotFoundError:
            self.users.append(user)
            return user
        raise UserAlreadyExistsError()

    def find(self, username) -> User:
        try:
            return next(x for x in self.users if x == User(username=username))
        except StopIteration:
            raise UserNotFoundError()
