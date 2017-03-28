from collections import namedtuple
from simplejson import dumps


class EntityReport(namedtuple("EntityReport", ("id", "lat", "xlong", "source_name", "category",
                                               "speed", "course", "elevation", "nationality", "picture_url", "height",
                                               "nickname"))):
    def to_json(self):
        return dumps(self, namedtuple_as_object=True)
