from Reporter.reporter import Reporter
from EntityReport.entity_report_factory import EntityReportFactory
from EntityReport.entity_report_update import EntityReportUpdate


class ReportGenerator:
    def __init__(self, _entity_report_factory
                     , _entity_report_update
                     , _number_of_reports
                     , _reporter
                     , _report_freq=1.0):
        """
        :type _number_of_reports: int
        :type _reporter: Reporter
        """
        assert isinstance(_entity_report_factory, EntityReportFactory)
        assert isinstance(_entity_report_update, EntityReportUpdate)
        assert isinstance(_reporter, Reporter)

        self.entity_report_factory = _entity_report_factory
        self.entity_report_update = _entity_report_update
        self.number_of_reports = _number_of_reports
        self.report_freq = _report_freq
        self.reporter = _reporter

    def generate(self):
        for i in range(self.number_of_reports):
            entity_report = self.entity_report_factory.create()
            self.reporter.report(entity_report)
