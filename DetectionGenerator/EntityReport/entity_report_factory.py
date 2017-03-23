from entity_report import EntityReport


class EntityReportFactory:
    def __init__(self, _entity_id_generator, _location_generator):
        self.entity_id_generator = _entity_id_generator
        self.location_generator = _location_generator

    def create(self):
        # type: () -> EntityReport
        location = self.location_generator.generate()
        return EntityReport(self.entity_id_generator.generate(),
                            location.lat,
                            location.long)
