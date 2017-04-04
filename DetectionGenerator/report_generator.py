from Reporter.reporter import Reporter
from entities_manager import EntitiesManager
from utils.logger_util import log
import time


class ReportGenerator:
    def __init__(self, _entity_manager
                     , _number_of_reports
                     , _reporter
                     , _report_freq=1):
        """
        :type _number_of_reports: int
        :type _reporter: Reporter
        :type _entity_manager: EntitiesManager
        :type _report_freq: int
        """
        assert isinstance(_reporter, Reporter)
        assert isinstance(_entity_manager, EntitiesManager)

        self.number_of_reports = _number_of_reports
        self.report_freq = _report_freq
        self.reporter = _reporter
        self.entity_manager = _entity_manager
        self.reports_total = 0

    def _calculate_wait_time(self, elapsed_time):
        wait_time = (1.0/self.report_freq) - elapsed_time
        if wait_time < 0:
            return 0
        return wait_time

    def single_generation(self):
        entities_reports = self.entity_manager.generate_updates(self.number_of_reports)
        self.reports_total = self.reports_total + len(entities_reports)

        for report in entities_reports:
            log().debug("Reporting update on entity:" + report)
            self.reporter.report(report)
        self.reporter.end_reporting()

    def generate(self):
        freq_count = 0.0
        last_round_time = time.time()

        while True:
            start_generation_time = time.time()

            # Monitoring over full seconds reports
            if freq_count == self.report_freq:
                log().info("Current number of reports:" + str(self.reports_total) +
                           " in " + str(time.time() - last_round_time) + " sec")
                self.reports_total = 0
                freq_count = 0
                last_round_time = time.time()
            freq_count = freq_count + 1

            self.single_generation()
            end_generation_time = time.time()
            time.sleep(self._calculate_wait_time(end_generation_time - start_generation_time))
