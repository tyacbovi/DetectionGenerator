from entities_pool import EntitiesPool
from redis import Redis


class EntitiesPoolRedis(EntitiesPool):
    def __init__(self, _redis_connection):
        assert isinstance(_redis_connection, Redis)
        self.redis_connection = _redis_connection

    def store_entity_json(self, entity_id, entity_json):
        self.redis_connection.set(entity_id, entity_json)

    def get(self, entity_id):
        return self.redis_connection.get(entity_id)

    def get_all_keys_iter(self):
        return self.redis_connection.scan_iter()

    def get_keys_size(self):
        return self.redis_connection.dbsize()
