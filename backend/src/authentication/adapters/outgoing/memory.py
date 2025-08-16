from authentication.domain.model.user import User
from authentication.domain.port.outgoing import UserNotFoundError, UserRepository


class InMemoryUserRepository(UserRepository):
    def __init__(self):
        self.users = []

    def add(self, user: User) -> User:
        self.users.append(user)
        return user

    def find(self, username) -> User:
        try:
            return next(x for x in self.users if x == User(username=username))
        except StopIteration:
            raise UserNotFoundError()
