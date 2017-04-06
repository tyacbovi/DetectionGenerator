from entity_report import EntityReport
import time


class EntityReportUpdate:
    def __init__(self, _location_generator):
        self.location_generator = _location_generator

    def update(self, entity_report):
        assert isinstance(entity_report, EntityReport)
        new_location = self.location_generator.generate()

        return EntityReport(entity_report.id, new_location.lat, new_location.long, entity_report.source_name,
                            entity_report.category, entity_report.speed, entity_report.course,  entity_report.elevation,
                            entity_report.nationality, entity_report.picture_url, entity_report.height,
                            entity_report.nickname, time.time())


