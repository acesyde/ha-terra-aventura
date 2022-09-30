"""PyTerraAventura API Client."""
from __future__ import annotations

from types import TracebackType
from typing import Any

from aiohttp import ClientSession
import aiohttp

from .exceptions import BadCredentialsException

from .const import (
    APP_VERSION,
    BASE_URL,
    LOGIN_ENDPOINT,
    API_TIMEOUT_SECONDS,
    USER_ENDPOINT,
)


class TerraAventuraClient:
    """Interface class for the Terra Aventura API."""

    session: ClientSession

    def __init__(
        self,
        session: ClientSession | None = None,
    ) -> None:
        """Initialize TerraAventuraClient."""

        self.session = (
            session if session else ClientSession(timeout=API_TIMEOUT_SECONDS)
        )

    async def __aenter__(self) -> TerraAventuraClient:
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        await self.session.close()

    async def authenticate(self, username: str, password: str) -> Any:
        """Log user."""

        async with self.session.post(
            BASE_URL + LOGIN_ENDPOINT,
            json={"name": username, "pass": password},
        ) as response:
            result = await response.json()

            if response.status == 400:
                raise BadCredentialsException()

            return result

    async def get_user(self, uid: str, username: str, password: str) -> Any:
        """Return user informations."""

        async with self.session.get(
            BASE_URL + USER_ENDPOINT.format(uid, APP_VERSION),
            auth=aiohttp.BasicAuth(username, password),
        ) as response:
            result = await response.json()

            return result
