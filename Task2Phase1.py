# Application that fetches weather data using an API and displays it to the user

# Written by Rahul Joshi

# First we import necessary libraries
import os
import requests

# Now load environment variables
API_KEY = '2ea578054960231799e59c3a0f0bf448'
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

# Get the city name from the user
city = input('Enter the name of the city: ')

# Construct the API request URL using f-strings
request_url = f"{BASE_URL}?q={city}&appid={API_KEY}"

# Send a GET request to the API
response = requests.get(request_url)

# Check if the request was successful (status code 200)
if response.status_code == 200:

    # Parse the JSON response
    data = response.json()

    # Extract weather description and temperature
    weather_description = data['weather'][0]['description']
    temperature_in_celsius = data["main"]["temp"] - 273.15  # Convert from Kelvin to Celsius

    # Display the weather information
    print('Weather: ', weather_description)
    print(f'Temperature: {temperature_in_celsius:.2f} °C')

else:
    # Handle the case where there's an error with the API request
    print('Error: Unable to retrieve weather data for the city.')
