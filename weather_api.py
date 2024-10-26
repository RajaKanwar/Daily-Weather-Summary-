import requests
from datetime import datetime
import schedule
import time

API_KEY = "c608a668c0257e304e72c6eacc7dbb50"

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def fetch_weather_data(city):
    
    API_URL = f"https://api.openweathermap.org/data/2.5/weather?q={city},IN&appid={API_KEY}"
    
    response = requests.get(API_URL)
    data = response.json()
    print(f"raw data {data}")
    if response.status_code == 200:
        return {
            'city': city,
            'temp': kelvin_to_celsius(data['main']['temp']),
            'feels_like': kelvin_to_celsius(data['main']['feels_like']),
            'condition': data['weather'][0]['main'],
            'timestamp': data['dt'],
            'humidity' : data['main']['humidity'],
            'wind_speed' : data['wind']['speed']
        }
    else:
        print(f"Failed to fetch data for {city}: {data.get('message')}")
        return None
    