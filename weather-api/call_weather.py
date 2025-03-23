import requests
from configparser import ConfigParser
#import configparser
import json

#use html paser for html pages
parser = ConfigParser()
parser.read("config.ini")

api_key = parser.get("WEATHER_API_DATA","api-key")

weather_url = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}&appid={api_key}"

req = requests.get(weather_url)

#print(api_key)