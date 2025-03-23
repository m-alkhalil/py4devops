import requests

# weather_url = ""
url = "https://xkcd.com/353/"
img = "https://imgs.xkcd.com/comics/python.png"

req = requests.get(url)
img_req = requests.get(img)

#print(dir(req))
#print(help(req))
#print(req.status_code)
#print(req.content)
#print(req.text)

try:
    with open("pic.png","wb") as img_f:
        img_f.write(img_req.content)
        print("file downloaded..")
except FileExistsError :
    print("Error")