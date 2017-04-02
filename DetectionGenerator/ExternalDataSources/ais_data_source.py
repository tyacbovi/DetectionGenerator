from urllib3.exceptions import InsecureRequestWarning
import urllib3
import json
from DetectionGenerator.EntityReport.entity_report import EntityReport

headers = {'Accept': '*/*',
           'Referer': 'https://www.marinetraffic.com/il/ais/home/centerx:37/centery:32/zoom:7',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
            'Connection': 'keep-alive',
            'Cookie': 'CAKEPHP=2j69ddi23dv4drqeprtd4054d3; SERVERID=vmwww1; _pendo_meta.915388fa-afe0-454c-6270-7a41b245e92e=599000508; _pendo_visitorId.915388fa-afe0-454c-6270-7a41b245e92e=_PENDO_T_RaiyZ7axrqh; __gads=ID=81252b8ebccd04af:T=1491134177:S=ALNI_MbqlHDpARn3VIlS9WIxUr_vz-oYdw; vTo=1; _ga=GA1.2.482281353.1491134169; _gat=1',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Language': 'en-US,en;q=0.8,he;q=0.6',
            'Accept-Encoding': 'gzip, deflate, sdch, br'
           }

urls = {'https://www.marinetraffic.com/getData/get_data_json_4/z:7/X:38/Y:25/station:0',
        'https://www.marinetraffic.com/getData/get_data_json_4/z:7/X:38/Y:26/station:0',
        'https://www.marinetraffic.com/getData/get_data_json_4/z:7/X:37/Y:25/station:0',
        'https://www.marinetraffic.com/getData/get_data_json_4/z:7/X:39/Y:25/station:0',
        'https://www.marinetraffic.com/getData/get_data_json_4/z:7/X:37/Y:26/station:0',
        'https://www.marinetraffic.com/getData/get_data_json_4/z:7/X:39/Y:26/station:0'
        }


class AISDataSource:
    def __init__(self):
        self.http = urllib3.PoolManager()
        urllib3.disable_warnings(InsecureRequestWarning)

    @staticmethod
    def filter_ship_by_cord(lat, xlong):
        return (lat <= 34.7416 and xlong <= 35.8525) and (lat <= 34.7416 and xlong >= 33.8) and (
            lat >= 28.2861 and xlong >= 33.8) and (lat >= 28.2861 and xlong <= 35.8525)

    @staticmethod
    def _convert_to_entity_report(ship_json):
        return EntityReport(lat=ship_json["LAT"],
                            xlong=ship_json["LON"],
                            speed=ship_json["SPEED"],
                            course=ship_json["COURSE"],
                            nickname=ship_json["SHIPNAME"],
                            id=ship_json["SHIP_ID"],
                            category="boat",
                            source_name="marine_traffic",
                            elevation=0,
                            nationality="SPAIN",
                            picture_url="",
                            height=0)

    def _retrieve_ais_data(self):
        """
        {"LAT":"-7.0999999999999996",
        "LON":"-62.868000000000002",
        "SPEED":"95",
        "COURSE":"8",
        "SHIPNAME":"[SAT-AIS]",
        "SHIPTYPE":"3",
        "SHIP_ID":"56455675839645",
        "TYPE_NAME":"Tugs & Special Craft"}
        :return list: 
        """
        res = []
        for url in urls:
            entities_in_area = json.loads(self.http.request(method='GET', url=url, headers=headers).data)['data']['rows']
            res.append(entities_in_area)
        return res

    def generate_updates(self):
        entities_reports = []
        for entities_list in self._retrieve_ais_data():
            for entity in entities_list:
                entity_report = self._convert_to_entity_report(entity)
                if self.filter_ship_by_cord(entity_report.lat, entity_report.xlong):
                    entities_reports.append(entity_report)
        return entities_reports
