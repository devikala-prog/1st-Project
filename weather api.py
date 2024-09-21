import datetime as dt
import requests

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY =  "672dc0b17196b644cbda84a46d03477a" 
CITY = input("enter CITY name : ")  

def kelvin_to_celsius_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9/5) + 32
    return celsius, fahrenheit

url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY
response = requests.get(url).json()

if response.get("cod") != 200:
    print(f"Error fetching weather data: {response.get('message')}")
else:
    temp_kelvin = response['main']['temp']
    temp_celsius, temp_fahrenheit = kelvin_to_celsius_fahrenheit(temp_kelvin)

    feels_like_kelvin = response['main']['feels_like']
    feels_like_celsius, feels_like_fahrenheit = kelvin_to_celsius_fahrenheit(feels_like_kelvin)

    wind_speed = response['wind']['speed']
    humidity = response['main']['humidity']
    description = response['weather'][0]['description']

    timezone_offset = response['timezone']
   
    sunrise_time = dt.datetime.fromtimestamp(response['sys']['sunrise'] + timezone_offset, tz=dt.timezone.utc)
    sunset_time = dt.datetime.fromtimestamp(response['sys']['sunset'] + timezone_offset, tz=dt.timezone.utc)

    print(f"Temperature in {CITY}: {temp_celsius:.2f}°C or {temp_fahrenheit:.2f}°F")
    print(f"Feels like: {feels_like_celsius:.2f}°C or {feels_like_fahrenheit:.2f}°F")
    print(f"Humidity in {CITY}: {humidity}%")
    print(f"Wind speed in {CITY}: {wind_speed} m/s")
    print(f"General weather in {CITY}: {description}")
    print(f"Sunrise in {CITY} at {sunrise_time} UTC.")
    print(f"Sunset in {CITY} at {sunset_time} UTC.")
