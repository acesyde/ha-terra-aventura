"""Terra Aventura Sensors."""

from dataclasses import dataclass
from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.components.sensor import (
    SensorEntity,
    SensorEntityDescription,
)
from homeassistant.helpers.update_coordinator import (
    CoordinatorEntity,
    DataUpdateCoordinator,
)

from .const import DOMAIN, COORDINATOR


@dataclass
class TerraAventuraSensorEntityDescriptionMixin:
    """Mixin for required keys."""

    data_path: str


@dataclass
class TerraAventuraSensorEntityDescription(
    SensorEntityDescription, TerraAventuraSensorEntityDescriptionMixin
):
    """Describes Meteo-France sensor entity."""


SENSOR_TYPES: tuple[TerraAventuraSensorEntityDescription, ...] = (
    TerraAventuraSensorEntityDescription(
        key="caches_total",
        name="Total caches",
        entity_registry_enabled_default=False,
        data_path="field_statistics:cachesTotales",
    ),
    TerraAventuraSensorEntityDescription(
        key="caches_discovered",
        name="Caches discovered",
        entity_registry_enabled_default=False,
        data_path="field_statistics:cachesUser",
    ),
    TerraAventuraSensorEntityDescription(
        key="jokers",
        name="Jokers",
        entity_registry_enabled_default=False,
        data_path="field_jokers",
    ),
)


class TerraAventuraSensor(CoordinatorEntity, SensorEntity):
    """Representation of a Terra Aventura sensor."""

    entity_description: TerraAventuraSensorEntityDescription

    def __init__(
        self,
        coordinator: DataUpdateCoordinator,
        description: TerraAventuraSensorEntityDescription,
    ) -> None:
        """Initialize the Terra Aventura sensor."""
        super().__init__(coordinator)
        self.entity_description = description


async def async_setup_entry(
    hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback
) -> None:
    """Set up the Terra Aventura sensors from a config entry."""

    coordinator = hass.data[DOMAIN][entry.entry_id][COORDINATOR]

    entities = [
        TerraAventuraSensor(coordinator, description) for description in SENSOR_TYPES
    ]

    async_add_entities(entities, False)
