from location import Location
from random import random


class LocationGenerator:
    def __init__(self):
        pass

    @staticmethod
    def generate(base_lat=32, base_long=34):
        return Location(base_lat + random(), base_long + random())
