from entity_report import EntityReport


class EntityReportUpdate:
    def __init__(self, _location_generator):
        self.location_generator = _location_generator

    def update(self, entity_report):
        assert isinstance(entity_report, EntityReport)
        entity_report.location_lat, entity_report.location_long = self.location_generator.generate()
