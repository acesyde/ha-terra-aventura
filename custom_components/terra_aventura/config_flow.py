"""Adds config flow for Terra Aventura."""

from typing import Any

from homeassistant import config_entries
from homeassistant.const import CONF_USERNAME, CONF_PASSWORD
from homeassistant.helpers.aiohttp_client import async_get_clientsession
import voluptuous as vol
from async_timeout import timeout

from custom_components.terra_aventura.pyterraaventura.client import TerraAventuraClient
from custom_components.terra_aventura.pyterraaventura.exceptions import (
    BadCredentialsException,
)

from .const import DOMAIN, LOGGER


class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Config flow for Terra Aventura."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Handle a flow initialized by the user."""
        errors = {}

        if user_input is not None:
            websession = async_get_clientsession(self.hass)
            try:
                async with timeout(10):
                    terraAventuraClient = TerraAventuraClient(websession)
                    await terraAventuraClient.authenticate(
                        user_input[CONF_USERNAME], user_input[CONF_PASSWORD]
                    )
            # Except invalid login or password
            except BadCredentialsException as exception:  # pylint: disable=broad-except
                errors["base"] = "bad_credentials"
                LOGGER.exception(exception)
            except Exception as exception:  # pylint: disable=broad-except
                errors["base"] = "unknown"
                LOGGER.exception(exception)
            else:
                await self.async_set_unique_id(
                    "123456", raise_on_progress=False  # Uuid
                )

                return self.async_create_entry(
                    title=user_input[CONF_USERNAME], data=user_input
                )

        return self.async_show_form(
            step_id="user",
            # description_placeholders={"url": NestClient.generate_token_url()},
            data_schema=vol.Schema(
                {
                    vol.Required(CONF_USERNAME): str,
                    vol.Required(CONF_PASSWORD): str,
                }
            ),
            errors=errors,
        )
