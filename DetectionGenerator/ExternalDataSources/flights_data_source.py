from urllib3.exceptions import InsecureRequestWarning
import time
import urllib3
import json
from DetectionGenerator.EntityReport.entity_report import EntityReport

headers = {'Accept': 'application/json, text/javascript, */*',
           'Referer': 'https://www.flightradar24.com/31.88,33.82/9',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
            'Accept-Language': 'en-US,en;q=0.8,he;q=0.6',
            'Accept-Encoding': 'gzip, deflate, sdch'
           }

url = 'https://data.flightradar24.com/zones/fcgi/feed.js?bounds=32.91166128274316,30.70856633173285,32.367455749512374,35.826416015625'


class FlightsDataSource:
    def __init__(self):
        self.http = urllib3.PoolManager()
        urllib3.disable_warnings(InsecureRequestWarning)

    @staticmethod
    def _convert_to_entity_report(entity, entity_id):
        return EntityReport(lat=entity[1],
                            xlong=entity[2],
                            speed=entity[5],
                            course=entity[3],
                            nickname=entity[13],
                            id=entity_id,
                            category="airplane",
                            source_name="flight_radar",
                            elevation=0,
                            nationality="SPAIN",
                            picture_url="",
                            height=entity[4])

    def _retrieve_flights_data(self):
        """
        :return dict: 
        """
        return json.loads(self.http.request(method='GET', url=url, headers=headers).data)

    def generate_updates(self):
        entities_reports = []
        for entity_id, entity in self._retrieve_flights_data().iteritems():
            if isinstance(entity, list):
                entities_reports.append(self._convert_to_entity_report(entity_id=entity_id,
                                                                       entity=entity))
        return entities_reports

start = time.time()
FlightsDataSource().generate_updates()
print (time.time() - start)