from homeassistant.components.sensor import SensorEntity
from homeassistant.helpers.entity import EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import HomeAssistantType, ConfigType, DiscoveryInfoType
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from pythermalcomfort.models import set_tmp
from homeassistant.const import TEMP_CELSIUS
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity import Entity
from .const import DOMAIN, CONF_TDB, CONF_TR, CONF_RH, CONF_V, CONF_CLO, CONF_MET, CONF_NAME

async def async_setup_entry(hass: HomeAssistant, entry, async_add_entities: AddEntitiesCallback):
    async_add_entities([SetComfortSensor(hass, entry)], True)

class SetComfortSensor(SensorEntity):
    def __init__(self, hass: HomeAssistant, entry):
        self.hass = hass
        self.entry = entry
        self._name = entry.data.get(CONF_NAME, "SET Comfort")
        self._unique_id = f"set_comfort_{self._name.lower().replace(' ', '_')}"
        self._unit_of_measurement = TEMP_CELSIUS
        self._state = None

    @property
    def name(self):
        return self._name

    @property
    def unique_id(self):
        return self._unique_id

    @property
    def unit_of_measurement(self):
        return self._unit_of_measurement

    @property
    def state(self):
        return self._state

    async def async_update(self):
        try:
            tdb = float(self.hass.states.get(self.entry.data[CONF_TDB]).state)
            tr = float(self.hass.states.get(self.entry.data[CONF_TR]).state)
            rh = float(self.hass.states.get(self.entry.data[CONF_RH]).state)
            v = float(self.hass.states.get(self.entry.data[CONF_V]).state)
            clo = float(self.hass.states.get(self.entry.data[CONF_CLO]).state)
            met = float(self.hass.states.get(self.entry.data[CONF_MET]).state)

            result = set_tmp(tdb=tdb, tr=tr, rh=rh, v=v, clo=clo, met=met)
            self._state = round(result["set"], 2)

        except Exception as e:
            self._state = None
            self._attr_extra_state_attributes = {"error": str(e)}
