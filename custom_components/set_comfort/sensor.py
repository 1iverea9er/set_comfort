from homeassistant.components.sensor import SensorEntity
from homeassistant.const import TEMP_CELSIUS

async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    async_add_entities([SetComfortSensor()])

class SetComfortSensor(SensorEntity):
    def __init__(self):
        self._state = None
        self._attr_name = "SET Comfort"
        self._attr_unit_of_measurement = TEMP_CELSIUS

    @property
    def state(self):
        return self._state

    def update(self):
        # Пример фиктивного значения SET
        self._state = 25.0
