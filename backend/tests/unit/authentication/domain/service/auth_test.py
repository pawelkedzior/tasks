from unittest import TestCase
from unittest.mock import MagicMock, patch

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
    user_repository = MagicMock()
    service = AuthenticationService(user_repository)
    service.verify_password = MagicMock(return_value=True)
    user = User(username="username", password="password")

    def test_looks_for_user_in_repository(self):
        self.service.attempt_authentication(self.user)

        self.user_repository.find.assert_called_with(self.user.username)

    def test_verifies_password(self):
        self.service.attempt_authentication(self.user)

        self.service.verify_password.assert_called()

    def test_returns_token_when_success(self):
        expected_token = "token"
        with patch(
            "authentication.domain.service.auth.create_access_token",
            MagicMock(return_value=expected_token),
        ):
            token = self.service.attempt_authentication(self.user)

            assert token == expected_token

    def test_throws_AuthenticationError_when_user_not_found(self):
        user_repository = MagicMock()
        service = AuthenticationService(user_repository)
        service.user_repository.find = MagicMock(side_effect=UserNotFoundError)

        with self.assertRaises(AuthenticationError):
            service.attempt_authentication(self.user)

    def test_throws_AuthenticationError_when_wrong_password(self):
        service = AuthenticationService(self.user_repository)
        service.verify_password = MagicMock(return_value=False)

        with self.assertRaises(AuthenticationError):
            service.attempt_authentication(self.user)


class TestAuthenticationServiceRegisterUser(TestCase):
    user_repository = MagicMock()
    service = AuthenticationService(user_repository)

    def test_throws_when_user_already_exists(self):
        user = User(username="username", password="password")
        self.user_repository.add = MagicMock(side_effect=UserAlreadyExistsError())

        with self.assertRaises(UserAlreadyExistsError):
            self.service.register_new_user(user)

    def test_registers_new_user(self):
        user = User(username="username", password="password")

        self.service.register_new_user(user)

        self.user_repository.add.assert_called_with(user)
