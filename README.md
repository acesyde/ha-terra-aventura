[![hacs_badge](https://img.shields.io/badge/HACS-Default-orange.svg)](https://github.com/custom-components/hacs)
[![GitHub release](https://img.shields.io/github/release/acesyde/ha-terra-aventura.svg)](https://GitHub.com/acesyde/ha-terra-aventura/releases/)
[![Open in Visual Studio Code](https://open.vscode.dev/badges/open-in-vscode.svg)](https://open.vscode.dev/acesyde/ha-terra-aventura/)

# Terra Aventura integration for Home Assistant (work in progress)

## Installation

You can install this integration via [HACS](#hacs) or [manually](#manual).

### HACS

Add the repository url below to HACS, search for the Terra Aventura integration and choose install.

> https://github.com/acesyde/ha-terra-aventura

Reboot Home Assistant and configure the Terra Aventura integration via the integrations page or press the blue button below.

[![Open your Home Assistant instance and start setting up a new integration.](https://my.home-assistant.io/badges/config_flow_start.svg)](https://my.home-assistant.io/redirect/config_flow_start/?domain=terra_aventura)

### Manual

Copy the `custom_components/terra_aventura` to your custom_components folder. Reboot Home Assistant and configure the Terra Aventura integration via the integrations page or press the blue button below.

[![Open your Home Assistant instance and start setting up a new integration.](https://my.home-assistant.io/badges/config_flow_start.svg)](https://my.home-assistant.io/redirect/config_flow_start/?domain=terra_aventura)

## Advanced

### Enable debug logging

The [logger](https://www.home-assistant.io/integrations/logger/) integration lets you define the level of logging activities in Home Assistant. Turning on debug mode will show more information about unsupported devices in your logbook.

```
logger:
  default: critical
  logs:
    custom_components.terra_aventura: debug
```