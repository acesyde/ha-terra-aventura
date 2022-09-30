"""Constants for Terra Aventura."""
from __future__ import annotations
from datetime import timedelta

import logging
from typing import Final

from homeassistant.const import Platform

LOGGER: logging.Logger = logging.getLogger(__package__)

DOMAIN: Final = "terra_aventura"

PLATFORMS: list[Platform] = [Platform.SENSOR]

COORDINATOR = "coordinator"
SCAN_INTERVAL = timedelta(hours=3)
