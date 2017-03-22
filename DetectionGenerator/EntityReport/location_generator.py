from location import Location
from random import random


class LocationGenerator:
    def __init__(self):
        pass

    @staticmethod
    def generate():
        return Location(random(), random())
