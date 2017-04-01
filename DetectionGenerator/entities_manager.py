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
        # Recover from DB
        self.all_entities_reports = []
        for entity_id, entity in self.db_connection:
            self.all_entities_reports.append(EntityReport(**loads(entity_id)))

    def generate_updates(self, number_of_reports):
        json_reports = []
        for i, entity in enumerate(self.all_entities_reports):
            self.all_entities_reports[i] = self.update_factory.update(entity)
            json_report = self.all_entities_reports[i].to_json()
            json_reports.append(json_report)
            self.db_connection.put(key=self.all_entities_reports[i].id, value=json_report)

        num_of_entities = len(self.all_entities_reports)
        if num_of_entities < number_of_reports:
            for _ in range(number_of_reports - num_of_entities):
                new_entity = self.creation_factory.create(self.source_name)
                self.all_entities_reports.append(new_entity)
                json_report = new_entity.to_json()
                json_reports.append(json_report)
                self.db_connection.put(key=new_entity.id, value=json_report)

        return json_reports
