import requests
from configparser import ConfigParser
#import configparser
#import json

#SEE Basic Authentication

#use html paser for html pages
parser = ConfigParser()
parser.read("config.ini")

api_key = parser.get("WEATHER_API_DATA","api-key")
# Don't add paramerers to the url directly, instead creare a dict and let requests lib generate the appropreate url for us 
# it let us pass the parms as a dict
payload = {'q': 'Oak Lawn,Il,US','limit':1, 'appid':api_key}


#weather_url = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}&appid={api_key}"
url = "http://api.openweathermap.org/geo/1.0/direct"#?q=London&limit=5&appid={api_key}
req = requests.get(url,payload)

# with  open("data.json", "w") as f:
#         json.dump(req.json(),f,indent=4)

res_dict = {}
res_dict = req.json()# returns a dictionary         
print(res_dict)
# print(req.url)
# print(req.text)
# print(req.headers)
#print(api_key)

