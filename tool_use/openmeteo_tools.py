import requests
from typing import List, Dict, Any
from pydantic import BaseModel, Field

class GeocodeInput(BaseModel):
    name: str = Field(..., description="Nombre del lugar, e.g. 'Colmenar Viejo, Madrid'")

class GeocodeResult(BaseModel):
    latitude: float
    longitude: float
    elevation: float = 0.0
    name: str

def geocode_location(params: GeocodeInput) -> GeocodeResult:
    """Tool: busca coordenadas geográficas para un lugar."""
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={params.name}&count=1&language=es&format=json"
    resp = requests.get(url, timeout=5).json()
    if resp.get('results'):
        result = resp['results'][0]
        return GeocodeResult(
            latitude=result['latitude'],
            longitude=result['longitude'],
            elevation=result.get('elevation', 0),
            name=result['name']
        )
    raise ValueError(f"Lugar '{params.name}' no encontrado")

class ForecastInput(BaseModel):
    latitude: float = Field(..., description="Latitud del lugar")
    longitude: float = Field(..., description="Longitud del lugar")
    hourly: List[str] = Field(default_factory=lambda: ["temperature_2m", "precipitation_probability"], description="Variables horarias a pedir")
    forecast_days: int = Field(default=1, ge=1, le=7, description="Días de pronóstico")

class ForecastResult(BaseModel):
    location: str  # Añadido para claridad
    time: List[str]
    temperature_2m: List[float]
    precipitation_probability: List[float]

def get_weather_forecast(params: ForecastInput) -> ForecastResult:
    """Tool: pronóstico horario de variables meteorológicas."""
    params_dict = {
        "latitude": params.latitude,
        "longitude": params.longitude,
        # No tengo claro qué es "hourly"
        "hourly": ",".join(params.hourly),
        "forecast_days": params.forecast_days,
        "timezone": "auto"
    }
    url = "https://api.open-meteo.com/v1/forecast"
    resp = requests.get(url, params=params_dict, timeout=10).json()
    
    hourly = resp['hourly']
    return ForecastResult(
        location=f"{params.latitude:.4f}, {params.longitude:.4f}",
        time=hourly['time'],
        temperature_2m=hourly['temperature_2m'],
        precipitation_probability=hourly['precipitation_probability']
    )