# Thermal Comfort (SET) - Home Assistant Integration

This is a custom integration for [Home Assistant](https://www.home-assistant.io/) that calculates the **Standard Effective Temperature (SET)** using the **Pierce two-node model**, via the [`pythermalcomfort`](https://github.com/CenterForTheBuiltEnvironment/comfort_tool) library.

## 📦 Features

- Calculates SET using indoor climate sensors
- Based on ISO 7730 and ASHRAE 55 principles
- Provides a virtual sensor with real-time SET updates
- Configurable through the Home Assistant UI

## 📥 Installation via HACS

1. Go to **HACS → Integrations**
2. Click the three dots (⋮) → **Custom repositories**
3. Enter repository URL: `https://github.com/yourusername/set_comfort`
4. Category: `Integration`
5. Click **Add**
6. Find `SET Comfort` in HACS and install it
7. Restart Home Assistant

## ⚙️ Configuration

After installation, go to **Settings → Devices & Services → Add Integration**, then search for `SET Comfort` and configure it:

- **Name** — Optional name of the virtual sensor
- **tdb** — Dry bulb temperature sensor (°C)
- **tr** — Mean radiant temperature sensor (°C)
- **rh** — Relative humidity sensor (%)
- **v** — Air velocity sensor (m/s)
- **clo** — Clothing insulation (clo)
- **met** — Metabolic rate (met)

## 📚 References
- ISO 7730:2005 Appendix A
- ASHRAE Standard 55
- [Pierce Two-Node Model (CBE)](https://comfort.cbe.berkeley.edu/)

## 🧪 Future Improvements
- Sensation/Comfort classification sensor (e.g., "Slightly Warm")
- Automatic PMV/PPD calculation
- Calibration with user feedback ("golden standard")

## 📝 License
[MIT](LICENSE)

---
Maintained by `1iverea9er`
