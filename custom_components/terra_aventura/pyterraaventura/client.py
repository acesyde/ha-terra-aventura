"""PyTerraAventura API Client."""
from __future__ import annotations

from types import TracebackType
from typing import Any
import urllib.parse
from wsgiref import headers

from aiohttp import ClientSession, FormData

from .exceptions import BadCredentialsException

from .const import BASE_URL, LOGIN_PATH, LOGGER, API_TIMEOUT_SECONDS
from .models import TerraAventuraLoginResponse


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

    async def authenticate(
        self, username: str, password: str
    ) -> TerraAventuraLoginResponse:
        """Log user."""

        async with self.session.post(
            BASE_URL + LOGIN_PATH,
            json={"name": username, "pass": password},
        ) as response:
            result = await response.json()

            if response.status == 400:
                raise BadCredentialsException()

            return result
