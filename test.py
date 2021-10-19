# Import libraries
import requests
import os
import json

# Get api key from environment variables
API_KEY = os.environ['MAPS_KEY']

class APIReq:
    """Class to handle api requests to the maps api"""

    def __init__(self, key: str) -> None:
        """Initialiser of the APIReq class"""
        # Save api key as self.key
        self.key = {"key": key}

    def place_from_name(self, name: str) -> dict:
        """Function to find a place by its name as a string"""
        url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json"

        params = {
            "input": name,
            "inputtype": "textquery"
        }

        params.update(self.key)

        info = requests.get(url, params=params).json()

        return info

    def info_from_id(self, p_id: str) -> dict:
        """Function to find details about a place from its id"""
        url = "https://maps.googleapis.com/maps/api/place/details/json"

        params = {
            "placeid": p_id
        }

        params.update(self.key)

        info = requests.get(url, params).json()

        return info

    def find_nearby(self, latitude: float, longitude: float, radius: int) -> dict:
        """Function to find nearby things from a position and a radius"""
        url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"

        params = {
            "location": f"{latitude},{longitude}",
            "radius": radius
        }

        params.update(self.key)

        info = requests.get(url, params=params).json()

        return info

    def dist_matrix(self, destinations: list, origins: list, mode: str) -> dict:
        """Function to find distance and times between points as a matrix"""
        url = "https://maps.googleapis.com/maps/api/distancematrix/json"

        params = {
            "destinations": "|".join(destinations[:10]),
            "origins": "|".join(origins[:10]),
            "mode": mode
        }

        params.update(self.key)

        info = requests.get(url, params=params).json()

        return info

    @staticmethod
    def grab_info(info):
        return {
            "location": info['geometry']['location'],
            "name": info['name'],
            "place_id": info['place_id'],
            }

maps = APIReq(API_KEY)

start = maps.place_from_name("Ilkley")['candidates'][0]['place_id']
end = maps.place_from_name("Ben Rhydding")['candidates'][0]['place_id']

start_info = maps.grab_info(maps.info_from_id(start)['result'])
end_info = maps.grab_info(maps.info_from_id(end)['result'])

places = []
for place in maps.find_nearby(*start_info['location'].values(), 2500)['results']:
    places.append(maps.grab_info(place))

places = [place for place in places if place != start_info and place != end_info]

info = {
    "start": start_info,
    "end": end_info,
    "places": places
}

with open("info.json", "w") as f:
    print(json.dumps(info), file=f)