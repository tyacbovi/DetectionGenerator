from EntitiesPool.entities_pool import EntitiesPool
from EntityReport.entity_report_factory import EntityReportFactory
from EntityReport.entity_report_update import EntityReportUpdate
from EntityReport.entity_report import EntityReport
from simplejson import loads


class EntitiesManager:
    def __init__(self, _entity_pool, _creation_factory, _update_factory):
        assert isinstance(_entity_pool, EntitiesPool)
        assert isinstance(_creation_factory, EntityReportFactory)
        assert isinstance(_update_factory, EntityReportUpdate)

        self.creation_factory = _creation_factory
        self.update_factory = _update_factory
        self.entities_pool = _entity_pool

    def generate_updates(self, update_rate):
        all_entities_report = []
        for entity in self.entities_pool.get_all_keys_iter():
            entity_report = EntityReport(**loads(self.entities_pool.get(entity)))
            updated_entity_report = self.update_factory.update(entity_report)
            all_entities_report.append(updated_entity_report)
            self.entities_pool.store_entity_json(updated_entity_report.id, updated_entity_report.to_json())

        num_of_entities = self.entities_pool.get_keys_size()
        if num_of_entities != update_rate:
            for _ in range(update_rate - num_of_entities):
                new_entity = self.creation_factory.create()
                all_entities_report.append(new_entity)
                self.entities_pool.store_entity_json(new_entity.id, new_entity.to_json())

        return all_entities_report
