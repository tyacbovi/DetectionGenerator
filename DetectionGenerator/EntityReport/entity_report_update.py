from entity_report import EntityReport


class EntityReportUpdate:
    def __init__(self, _location_generator):
        self.location_generator = _location_generator

    def update(self, entity_report):
        assert isinstance(entity_report, EntityReport)
        new_location = self.location_generator.generate()
        return EntityReport(entity_report.id, new_location.lat, new_location.long)

