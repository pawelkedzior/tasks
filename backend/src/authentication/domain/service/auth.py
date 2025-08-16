from passlib.context import CryptContext

from authentication.domain.jwt.token import create_access_token
from authentication.domain.model.user import User
from authentication.domain.port.incoming import AuthService
from authentication.domain.port.outgoing import UserRepository


class AuthenticationService(AuthService):
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def __new__(cls, user_repository: UserRepository):
        if not hasattr(cls, "instance"):
            cls.instance = super(AuthenticationService, cls).__new__(cls)
        return cls.instance

    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def attempt_authentication(self, user: User) -> str:
        try:
            stored_user = self.user_repository.find(user.username)

            if not self.verify_password(user.password, stored_user.password):
                raise AuthenticationError()

            return create_access_token(user.username)
        except Exception:
            raise AuthenticationError

    def register_new_user(self, user: User):
        user.password = self.pwd_context.hash(user.password)
        self.user_repository.add_user(user)

    def verify_password(self, provided_password: str, stored_password: str) -> bool:
        return self.pwd_context.verify(provided_password, stored_password)


class AuthenticationError(Exception):
    """Exception raised when anything went wrong with authentication."""
