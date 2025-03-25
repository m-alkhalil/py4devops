import requests
from configparser import ConfigParser
import logging

#import configparser

#SEE Basic Authentication

#use html paser for html pages
parser = ConfigParser()
parser.read("config.ini")

api_key = parser.get("WEATHER_API_DATA","api-key")
# Don't add paramerers to the url directly, instead creare a dict and let requests lib generate the appropreate url for us 
# it let us pass the parms as a dict
payload = {'q': 'Oak Lawn,Il,US','limit':1, 'appid':api_key}


#
url = "http://api.openweathermap.org/geo/1.0/direct"#?q=London&limit=5&appid={api_key}
req = requests.get(url,payload)

# with  open("data.json", "w") as f:
#         json.dump(req.json(),f,indent=4)

#res_dict = {}
res_dict = req.json()[0] # returns a list         
print(res_dict)
print(type(res_dict))

print(res_dict['lon'])
print(res_dict['lat'])

# print(req.url)
# print(req.text)
# print(req.headers)
#print(api_key)

#### GET WEATHER
w_payload = {'lat':res_dict['lat'], 'lon':res_dict['lon'], 'appid':api_key}
weather_url = "https://api.openweathermap.org/data/2.5/weather"

w_req = requests.get (weather_url, w_payload)

d2 = w_req.json()

print(type(int(d2['main']['temp'])))