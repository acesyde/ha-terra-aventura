"""Constants used by PyTerraAventura."""
import logging

# Timeout other API calls after this number of seconds
API_TIMEOUT_SECONDS = 30

# Logger
LOGGER: logging.Logger = logging.getLogger(__package__)

# Base Terra Aventura Url
APP_VERSION = "3.2.0"
BASE_URL = "https://www.terra-aventura.fr"
LOGIN_ENDPOINT = "/user/login?langcode=fr&_format=json"
USER_ENDPOINT = "/app-user-get?uid={uid}&version={version}&langcode=fr&_format=json"
JOKER_ENDPOINT = "/app-jokers-config?langcode=fr&_format=json"
