import time
from DetectionGenerator.utils.logger_util import log


def event_loop(reporter, data_source):
    while True:
        start_fetch_time = time.time()
        entities_reports = data_source.generate_updates()
        for entity_report in entities_reports:
            reporter.report(entity_report)
        end_fetch_time = time.time()
        log().info("Reported " + str(len(entities_reports)) + " in " + str(end_fetch_time-start_fetch_time))
        time.sleep(1)  # Spacing requests flow
