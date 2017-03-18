from location import Location
from random import random


class LocationGenerator:
    def __init__(self):
        pass

    def generate(self):
        return Location(random(), random())
