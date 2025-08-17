from unittest import TestCase
from unittest.mock import MagicMock, patch

from authentication.adapters.outgoing.memory import InMemoryUserRepository
from authentication.domain.model.user import User
from authentication.domain.port.outgoing import (
    UserAlreadyExistsError,
    UserNotFoundError,
)
from authentication.domain.service.auth import (
    AuthenticationError,
    AuthenticationService,
)


class TestAuthenticationServiceAttemptAuthentication(TestCase):
    user = User(username="username", password="password")

    def test_looks_for_user_in_repository(self):
        user_repository = InMemoryUserRepository()
        service = AuthenticationService(user_repository)
        service.verify_password = MagicMock(return_value=True)
        user_repository.find = MagicMock(return_value=self.user)

        service.attempt_authentication(self.user)

        user_repository.find.assert_called_with(self.user.username)

    def test_verifies_password(self):
        user_repository = InMemoryUserRepository()
        service = AuthenticationService(user_repository)
        service.verify_password = MagicMock(return_value=True)

        service.attempt_authentication(self.user)

        service.verify_password.assert_called()

    def test_returns_token_when_success(self):
        user_repository = InMemoryUserRepository()
        service = AuthenticationService(user_repository)
        service.verify_password = MagicMock(return_value=True)
        user_repository.find = MagicMock(return_value=self.user)
        expected_token = "token"
        with patch(
            "authentication.domain.service.auth.create_access_token",
            MagicMock(return_value=expected_token),
        ):
            token = service.attempt_authentication(self.user)

            assert token == expected_token

    def test_throws_AuthenticationError_when_user_not_found(self):
        user_repository = InMemoryUserRepository()
        service = AuthenticationService(user_repository)
        user_repository.find = MagicMock(side_effect=UserNotFoundError)

        with self.assertRaises(AuthenticationError):
            service.attempt_authentication(self.user)

    def test_throws_AuthenticationError_when_wrong_password(self):
        user_repository = InMemoryUserRepository()
        user_repository.find = MagicMock(return_value=self.user)
        service = AuthenticationService(user_repository)
        service.verify_password = MagicMock(return_value=False)

        with self.assertRaises(AuthenticationError):
            service.attempt_authentication(self.user)


class TestAuthenticationServiceRegisterUser(TestCase):
    def test_throws_when_user_already_exists(self):
        user_repository = MagicMock()
        service = AuthenticationService(user_repository)
        user = User(username="username", password="password")
        user_repository.add_user = MagicMock(side_effect=UserAlreadyExistsError())

        with self.assertRaises(UserAlreadyExistsError):
            service.register_new_user(user)

    def test_registers_new_user(self):
        user_repository = MagicMock()
        service = AuthenticationService(user_repository)
        user = User(username="username", password="password")

        service.register_new_user(user)

        user_repository.add_user.assert_called_with(user)
