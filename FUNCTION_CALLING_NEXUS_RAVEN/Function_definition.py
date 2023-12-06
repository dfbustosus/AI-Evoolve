import requests

def get_coordinates_from_city(city_name):
    """
    Obtener lat/lon de una ciudad usando the Maps.co y Geocoding API.

    Args:
    city_name (str): El nombre de la ciudad.

    Returns:
    tuple: La lat/lon de la ciudad 
    """
    base_url = "https://geocode.maps.co/search"
    params = {"q": city_name}

    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        if data:
            # Asumiendo el primer resultado el mas relevante
            return data[0]["lat"], data[0]["lon"]
        else:
            return {"error": "No se encontro data para el nombre de ciudad"}
    else:
        return {"error": "Error al obtener la data, status code: {}".format(response.status_code)}

def get_weather_data(coordinates):
    """
    Obtener informacion de la Open-Meteo API data una lat y lon

    Args:
    coordinates (tuple): lat y lon de ubicación

    Returns:
    float: La temperatura actual de las coordenadas 
    """
    latitude, longitude = coordinates
    base_url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,wind_speed_10m",
        "hourly": "temperature_2m,relative_humidity_2m,wind_speed_10m"
    }

    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        print (f"""Temperature en C: {response.json()["current"]["temperature_2m"]}""")
    else:
        return {"error": "Error al obtener la data, status code: {}".format(response.status_code)}