from Reporter.reporter import Reporter
from entities_manager import EntitiesManager
from utils.logger_util import log


class ReportGenerator:
    def __init__(self, _entity_manager
                     , _number_of_reports
                     , _reporter
                     , _report_freq=1.0):
        """
        :type _number_of_reports: int
        :type _reporter: Reporter
        """
        assert isinstance(_reporter, Reporter)
        assert isinstance(_entity_manager, EntitiesManager)

        self.number_of_reports = _number_of_reports
        self.report_freq = _report_freq
        self.reporter = _reporter
        self.entity_manager = _entity_manager

    def generate(self):
        entities_reports = self.entity_manager.generate_updates(self.number_of_reports)
        print len(entities_reports)

        for report in entities_reports:
            log().debug("Reporting update on entity:" + report.id + " with the following " + report.to_json())
            self.reporter.report(report.to_json())
