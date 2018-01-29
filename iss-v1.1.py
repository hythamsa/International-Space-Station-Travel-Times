# Script to determine ISS travel time based on user's geo input
# Written and maintained by Hytham Abu-Safieh
# 
#

import requests, json
from pprint import pprint

def GetUserLoc():
    while True:
        try:
            location = str(raw_input("What is your location [Nearest City, Province/State, Country]? "))
        except ValueError:
            print ("Please be sure to enter a valid location. EG: Cambridge, England")
            continue
        if len(location) > 0:
            break
        else:
            print ("Please be sure to enter a valid location. EG: Cambridge, England")
    return location

def GetPass():
    while True:
        try:
            passes = int(raw_input("How many passes would you like to retrieve? "))
        except ValueError:
            print ("Please enter a number from 1 through 100.")
            continue
        if passes >=1 and passes <= 100:
            break
        else:
            print ("Please enter a number from 1 through 100")
    return passes


def GetLatLng():
    geocode = "https://maps.googleapis.com/maps/api/geocode/json"
    parameters = {"address": GetUserLoc(), "key": <input your Geocode API key here> }
    getlatlng = requests.get(geocode, params=parameters)
    return getlatlng

def iss():
    iss = "http://api.open-notify.org/iss-pass.json"
    data = json.loads(GetLatLng().content)
    lat = data["results"][0]["geometry"]["location"]["lat"]
    lng = data["results"][0]["geometry"]["location"]["lng"]

    latlng = {"lat": lat, "lon": lng, "n": GetPass()}

    getdata = requests.get(iss, params=latlng)
    parse_json = json.loads(getdata.content)
    pprint (parse_json["response"])

if __name__ == '__main__':
    iss()
