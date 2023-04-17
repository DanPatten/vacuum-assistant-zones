"""Google Assistant Vacuum Zones"""

import logging


from homeassistant.config_entries import ConfigEntry
from homeassistant.core import Config, HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady
from homeassistant.const import CONF_ENTITY_ID, CONF_SEQUENCE
import homeassistant.helpers.config_validation as cv
import voluptuous as vol

from .const import (
    DOMAIN,
    STARTUP_MESSAGE,
)

from . import trait

# CONFIG_SCHEMA = vol.Schema({
#     DOMAIN: vol.Schema({
#         vol.Required(CONF_ENTITY_ID): cv.entity_id,
#         vol.Required('zones'): {
#             cv.string: vol.Schema({
#                 vol.Optional('room'): vol.Any(list, int),
#                 vol.Optional('zone'): list,
#                 vol.Optional('repeats'): int,
#                 vol.Optional('goto'): list,
#                 vol.Optional('set_clean_motor_mode'): vol.Any()
#             })
#         }
#     })
# }, extra=vol.ALLOW_EXTRA)

_LOGGER = logging.getLogger(__name__)


async def async_setup(hass: HomeAssistant, _config: Config):
    """Set up this integration using YAML is not supported."""
    _LOGGER.info("vacuum-assistant-zones async_setup")
    if hass.data.get(DOMAIN) is None:
        hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN]['CONFIG'] = _config[DOMAIN]
    return True


#async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
   # _LOGGER.info("vacuum-assistant-zones async_setup_entry")

    # spa_identifier = None
    # spa_address = None
    # spa_name = None

    # if CONF_SPA_ADDRESS in entry.data:
    #     spa_address = entry.data.get(CONF_SPA_ADDRESS)
    # if CONF_SPA_NAME in entry.data:
    #     spa_name = entry.data.get(CONF_SPA_NAME)
    # spa_identifier = entry.data.get(CONF_SPA_IDENTIFIER)
    # client_id = entry.data.get(CONF_CLIENT_ID)

    # _LOGGER.debug(
    #     "Setup entry for UUID %s, ID %s, address %s (%s)",
    #     client_id,
    #     spa_identifier,
    #     spa_address,
    #     spa_name,
    # )

    # spaman = GeckoSpaManager(
    #     client_id,
    #     hass,
    #     entry,
    #     spa_identifier=spa_identifier,
    #     spa_address=spa_address,
    #     spa_name=spa_name,
    # )
    # await spaman.__aenter__()
    # # We always wait for the facade because otherwise the
    # # device info is not available for the first entity
    # if not await spaman.wait_for_facade():
    #     _LOGGER.error(
    #         "Failed to connect to spa %s address %s", spa_identifier, spa_address
    #     )
    #     raise ConfigEntryNotReady

    # hass.data[DOMAIN][entry.entry_id] = spaman

    # entry.async_on_unload(entry.add_update_listener(async_reload_entry))
    #return True