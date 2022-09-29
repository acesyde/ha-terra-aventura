"""Constants for Terra Aventura."""
from __future__ import annotations

import logging
from typing import Final

from homeassistant.const import Platform

LOGGER: logging.Logger = logging.getLogger(__package__)

DOMAIN: Final = "terra_aventura"

PLATFORMS: list[Platform] = [Platform.SENSOR]
