import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import callback
from homeassistant.const import CONF_NAME

DOMAIN = "set_comfort"

CONF_TDB = "tdb"
CONF_TR = "tr"
CONF_RH = "rh"
CONF_V = "v"
CONF_CLO = "clo"
CONF_MET = "met"

def build_schema(defaults):
    return vol.Schema({
        vol.Required(CONF_NAME, default=defaults.get(CONF_NAME, "SET Comfort")): str,
        vol.Required(CONF_TDB, default=defaults.get(CONF_TDB, "sensor.indoor_temperature")): str,
        vol.Required(CONF_TR, default=defaults.get(CONF_TR, "sensor.mean_radiant_temperature")): str,
        vol.Required(CONF_RH, default=defaults.get(CONF_RH, "sensor.humidity")): str,
        vol.Required(CONF_V, default=defaults.get(CONF_V, "sensor.air_velocity")): str,
        vol.Required(CONF_CLO, default=defaults.get(CONF_CLO, "sensor.clothing_insulation")): str,
        vol.Required(CONF_MET, default=defaults.get(CONF_MET, "sensor.metabolic_rate")): str,
    })

class SetComfortConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(self, user_input=None):
        errors = {}
        if user_input is not None:
            await self.async_set_unique_id(user_input[CONF_NAME])
            self._abort_if_unique_id_configured()
            return self.async_create_entry(title=user_input[CONF_NAME], data=user_input)

        return self.async_show_form(
            step_id="user",
            data_schema=build_schema({}),
            errors=errors
        )

class SetComfortOptionsFlowHandler(config_entries.OptionsFlow):
    def __init__(self, config_entry):
        self.config_entry = config_entry

    async def async_step_init(self, user_input=None):
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)

        return self.async_show_form(
            step_id="init",
            data_schema=build_schema(self.config_entry.data)
        )

@callback
def async_get_options_flow(config_entry):
    return SetComfortOptionsFlowHandler(config_entry)
