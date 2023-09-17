import os
import pprint
from dotenv import load_dotenv
import requests

load_dotenv()


def get_current_weather(city='Kampala'):

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={os.getenv('API_KEY')}&units=metric"
    response = requests.get(url).json()

    return response


if __name__ == '__main__':
    print("\n***Get Weather Condition***\n")
    city = input("Enter city name: ")
    if not bool(city.strip()):
        city = 'Kampala'
    weather_data = get_current_weather(city)
    pprint.pprint(weather_data)
