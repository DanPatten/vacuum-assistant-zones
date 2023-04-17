from homeassistant.components.google_assistant.trait import (
    StartStopTrait as _StartStopTrait,
    register_trait,
    TRAITS,
    COMMAND_STARTSTOP
)
from homeassistant.components import (vacuum)

from homeassistant.const import (
    ATTR_ENTITY_ID
)
import logging

_LOGGER = logging.getLogger(__name__)

from .const import (
    DOMAIN,
)

_LOGGER.info("Updating _StartStopTrait")

TRAITS.remove(_StartStopTrait)
@register_trait
class StartStopTrait(_StartStopTrait):

  
    def sync_attributes(self):
        _LOGGER.info("vacuum-assistant-zones sync_attributes")
        """Return StartStop attributes for a sync request."""
        attr = super().sync_attributes()
        if self.state.domain == vacuum.DOMAIN:
            #setup zones
            zones = []
            config = self.hass.data[DOMAIN]['CONFIG']

            # add rooms
            for key, value in config['zones'].items():
                zones.append(key)
            _LOGGER.info(zones)

            # add zones - TODO

            if len(zones) > 0:
                attr["availableZones"] = zones

        return attr

    
    async def execute(self, command, data, params, challenge):
        _LOGGER.info("vacuum-assistant-zones execute")
        """Execute a StartStop command."""
        domain = self.state.domain
        if domain == vacuum.DOMAIN and command == COMMAND_STARTSTOP and params["start"]:
            if "zone" in params or "multipleZones" in params:
                zones = []
                if "multipleZones" in params:
                    zones = params["multipleZones"]
                else:
                    zones.append(params["zone"])
                #setup zones
                zoneIds = []
                config = self.hass.data[DOMAIN]['CONFIG']
                for key, value in config['zones'].items():
                    if key in zones:
                        for key, value in value.items():
                            zoneIds.append(value)
                if len(zoneIds) > 0:
                    return await self.hass.services.async_call(
                            'xiaomi_miio',
                            'vacuum_clean_segment',
                            {
                                ATTR_ENTITY_ID: self.state.entity_id,
                                'segments': zoneIds
                            },
                            blocking=True,
                            context=data.context,
                    )

        return super().execute(command, data, params, challenge)