from unittest.mock import MagicMock, patch

import pytest

from authentication.adapters.incoming.controller import login, register_new_user

pytest_plugins = ("pytest_asyncio",)


@pytest.mark.asyncio
async def test_login__calls_service_method():
    with (
        patch("authentication.adapters.incoming.controller.app") as app,
        patch(
            "authentication.adapters.incoming.controller.authService"
        ) as auth_service,
    ):
        app.post = MagicMock(return_value=lambda x: x)

        await login()

        auth_service.attempt_authentication.assert_called()


@pytest.mark.asyncio
async def test_register_new_user__calls_service_method():
    with (
        patch("authentication.adapters.incoming.controller.app") as app,
        patch(
            "authentication.adapters.incoming.controller.authService"
        ) as auth_service,
    ):
        app.post = MagicMock(return_value=lambda x: x)

        await register_new_user()

        auth_service.register_new_user.assert_called()
