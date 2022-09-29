"""Constants used by PyTerraAventura."""
import logging

# Timeout other API calls after this number of seconds
API_TIMEOUT_SECONDS = 30

# Logger
LOGGER: logging.Logger = logging.getLogger(__package__)

# Base Terra Aventura Url
BASE_URL = "https://www.terra-aventura.fr"
LOGIN_PATH = "/user/login?langcode=fr&_format=json"
USER_PATH = "/app-user-get?uid=484376&version=3.2.0&langcode=fr&_format=json"
JOKER_PATH = "/app-jokers-config?langcode=fr&_format=json"
