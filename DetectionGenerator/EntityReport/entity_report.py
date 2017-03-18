class EntityReport:
    def __init__(self, _id, _location_lat, _location_long):
        self.id = _id
        self.location_lat = _location_lat
        self.location_long = _location_long

    @property
    def __str__(self):
        return "id:" + self.id + " , lat:" + str(self.location_lat) + " , long:" + str(self.location_long)
