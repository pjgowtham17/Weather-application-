# Weather-application-
import requests

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # You can change this to 'imperial' for Fahrenheit
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        
        if response.status_code == 200:
            temperature = data['main']['temp']
            description = data['weather'][0]['description']
            print(f"Current weather in {city}: {temperature}°C, {description}")
        else:
            print(f"Error: {data['message']}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Replace 'YOUR_API_KEY' with your actual API key from OpenWeatherMap
api_key = 'YOUR_API_KEY'
city_name = input("Enter city name: ")

get_weather(api_key, city_name)
