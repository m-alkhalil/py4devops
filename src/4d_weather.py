import requests
import json
from configparser import ConfigParser

con_p = ConfigParser()
con_p.read("../config/config.ini")
api_key =con_p.get("WEATHER_API_DATA","api-key")

payload = {
    'lat': 44.34,
    'lon': 10.99,
    'appid': api_key 
}
url= "https://api.openweathermap.org/data/2.5/forecast"

data2 = {
    'zip': "60453,US",
    'units': 'imperial',
    'appid': api_key 
}
url2 = "pi.openweathermap.org/data/2.5/forecast"

h_data = requests.get(url, data2)#(url,payload)
dt_data = h_data.json()
# print(dt_data)
lst = dt_data['list']
ite = None
for item in lst:
    ite = item
    break
print (ite['main']['temp'])
print (ite['dt_txt'])
# with open("data.json","w") as f :
#     json.dump(h_data.json(),f,indent=4)

all_data = []
# for item in lst:
#     all_data.append(item['main'])