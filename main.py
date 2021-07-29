import requests
import datetime


my_lat = 35.652832
my_lng = 139.839478
parameters = {
    "lat" : my_lat ,
    "lng" : my_lng,
    "formatted" : 0
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters, )
response.raise_for_status()
data = response.json()
print(data)
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0] #切到只剩下 幾點
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
print(sunset)
print(sunrise)

time = datetime.datetime.now()
print(time)