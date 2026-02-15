# tool_use/tools_catalog.py
from .openmeteo_tools import geocode_location, get_weather_forecast, GeocodeInput, ForecastInput

TOOLS_CATALOG = {
    "geocode_location": {
        "name": "geocode_location",
        "description": "Busca coordenadas (lat, lon, elevación) para cualquier lugar del mundo. Úsala SIEMPRE antes de pedir pronósticos.",
        "input_schema": GeocodeInput.model_json_schema(),
        "func": geocode_location
    },
    "get_weather_forecast": {
        "name": "get_weather_forecast",
        "description": "Obtiene pronóstico horario detallado (temperatura, probabilidad lluvia, etc.) para coordenadas específicas.",
        "input_schema": ForecastInput.model_json_schema(),
        "func": get_weather_forecast
    }
    # Añade aquí tools existentes si las hay
}
