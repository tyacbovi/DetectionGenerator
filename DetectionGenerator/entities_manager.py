from EntityReport.entity_report_factory import EntityReportFactory
from EntityReport.entity_report_update import EntityReportUpdate
from EntityReport.entity_report import EntityReport
from simplejson import loads
from plyvel import DB


class EntitiesManager:
    def __init__(self, _db_connection, _creation_factory, _update_factory, _source_name):
        assert isinstance(_db_connection, DB)
        assert isinstance(_creation_factory, EntityReportFactory)
        assert isinstance(_update_factory, EntityReportUpdate)
        assert isinstance(_source_name, str)

        self.creation_factory = _creation_factory
        self.update_factory = _update_factory
        self.db_connection = _db_connection
        self.source_name = _source_name

    def generate_updates(self, update_rate):
        all_entities_report = []
        snapshot = self.db_connection.snapshot()
        num_of_entities = 0

        for entity_id, entity in snapshot:
            num_of_entities = num_of_entities + 1
            entity_report = EntityReport(**loads(entity))
            updated_entity_report = self.update_factory.update(entity_report)
            all_entities_report.append(updated_entity_report)
            self.db_connection.put(key=updated_entity_report.id, value=updated_entity_report.to_json())

        if num_of_entities < update_rate:
            for _ in range(update_rate - num_of_entities):
                new_entity = self.creation_factory.create(self.source_name)
                all_entities_report.append(new_entity)
                self.db_connection.put(key=new_entity.id, value=new_entity.to_json())

        return all_entities_report
