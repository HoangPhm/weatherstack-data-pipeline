import requests
import os

api_key = os.environ.get("WEATHER_API_KEY") 
api_url = f"http://api.weatherstack.com/current?access_key={api_key}&query=New York"

def fetch_data():
    print("fetching data from Weatherstack API ...")
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        print('API Request received successfully')
        data = response.json()
        print(data)
        return data 
    except requests.exceptions.RequestException as e:
        print(f"An error occurred {e}")
        raise

def mock_fetch_data():
    return {'request': {'type': 'City', 'query': 'New York, United States of America', 'language': 'en', 'unit': 'm'}, 'location': {'name': 'New York', 'country': 'United States of America', 'region': 'New York', 'lat': '40.714', 'lon': '-74.006', 'timezone_id': 'America/New_York', 'localtime': '2026-06-04 23:38', 'localtime_epoch': 1780616280, 'utc_offset': '-4.0'}, 'current': {'observation_time': '03:38 AM', 'temperature': 23, 'weather_code': 113, 'weather_icons': ['https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0008_clear_sky_night.png'], 'weather_descriptions': ['Clear '], 'astro': {'sunrise': '05:26 AM', 'sunset': '08:23 PM', 'moonrise': '11:59 PM', 'moonset': '08:47 AM', 'moon_phase': 'Waning Gibbous', 'moon_illumination': 88}, 'air_quality': {'co': '172', 'no2': '70', 'o3': '36', 'so2': '2.4', 'pm2_5': '19.8', 'pm10': '21.9', 'us-epa-index': '2', 'gb-defra-index': '2'}, 'wind_speed': 7, 'wind_degree': 232, 'wind_dir': 'SW', 'pressure': 1017, 'precip': 0, 'humidity': 48, 'cloudcover': 0, 'feelslike': 25, 'uv_index': 0, 'visibility': 16, 'is_day': 'no'}}


