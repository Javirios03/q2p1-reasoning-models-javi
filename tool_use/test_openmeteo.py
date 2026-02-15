from openmeteo_tools import geocode_location, get_weather_forecast

# Test 1: Geocoding
geo = geocode_location({"name": "Colmenar Viejo, Madrid"})
print(f"Colmenar Viejo: lat={geo.latitude}, lon={geo.longitude}")

# Test 2: Forecast
forecast = get_weather_forecast({"latitude": geo.latitude, "longitude": geo.longitude})
print(f"Primeras 3 horas: {forecast.time[:3]}")
print(f"Temps: {forecast.temperature_2m[:3]}°C")
print(f"Lluvia %: {forecast.precipitation_probability[:3]}")
