import requests
import json


# weather_url = ""
url = "https://xkcd.com/353/"

req = requests.get(url)

#print(dir(req))
#print(help(req))
#print(req.status_code)
#print(req.content)