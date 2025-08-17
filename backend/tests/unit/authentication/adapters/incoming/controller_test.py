from unittest.mock import MagicMock, patch

import pytest

from authentication.adapters.incoming.controller import login, register_new_user
from authentication.domain.model.user import User

pytest_plugins = ("pytest_asyncio",)


@pytest.mark.asyncio
async def test_login__calls_service_method():
    with (
        patch("authentication.adapters.incoming.controller.app") as app,
        patch(
            "authentication.adapters.incoming.controller.auth_service"
        ) as auth_service,
    ):
        app.post = MagicMock(return_value=lambda x: x)
        user = User(username="user", password="password")

        await login(user)

        auth_service.attempt_authentication.assert_called_with(user)


@pytest.mark.asyncio
async def test_register_new_user__calls_service_method():
    with (
        patch("authentication.adapters.incoming.controller.app") as app,
        patch(
            "authentication.adapters.incoming.controller.auth_service"
        ) as auth_service,
    ):
        app.post = MagicMock(return_value=lambda x: x)
        user = User(username="user", password="password")

        await register_new_user(user)

        auth_service.register_new_user.assert_called_with(user)
