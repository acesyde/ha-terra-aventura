"""Terra Aventura Coordinator."""

from datetime import datetime
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator
from homeassistant.const import CONF_USERNAME, CONF_PASSWORD

from .sensor import TerraAventuraSensorEntityDescription
from .const import SCAN_INTERVAL, LOGGER

from .pyterraaventura.client import TerraAventuraClient


class TerraAventuraCoordinator(
    DataUpdateCoordinator[list[TerraAventuraSensorEntityDescription]]
):
    """DataUpdateCoordinator for Terra Aventura."""

    id: str
    username: str
    password: str
    hass: HomeAssistant

    def __init__(
        self,
        hass: HomeAssistant,
        client: TerraAventuraClient,
        entry: ConfigEntry,
    ) -> None:
        """Initialize DataUpdateCoordinator for Terra Aventura."""
        self.client = client
        self.last_update = datetime.utcnow()
        self.username = entry.data[CONF_USERNAME]
        self.password = entry.data[CONF_PASSWORD]
        self.hass = hass
        self.id = entry.unique_id
        super().__init__(
            hass,
            LOGGER,
            name="TerraAventura",
            update_interval=datetime.timedelta(seconds=SCAN_INTERVAL),
        )

    async def _async_update_data(self) -> list[TerraAventuraSensorEntityDescription]:
        """Get the data for Terra Aventura."""
        now = datetime.utcnow()

        try:
            result = await self.client.get_user(self.id, self.username, self.password)
        except Exception as error:
            raise ConfigEntryNotReady from error

        return None
