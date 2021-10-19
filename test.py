# Import libraries
import requests
import os

# Get api key from environment variables
API_KEY = os.environ['MAPS_KEY']

class APIReq:
    """Class to handle api requests to the maps api"""

    def __init__(self, key: str) -> None:
        """Initialiser of the APIReq class"""
        # Save api key as self.key
        self.key = {"key": key}

    def place_by_name(self, name: str) -> dict:
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

