from EntityReport.entity_report_factory import EntityReportFactory
from EntityReport.entity_report_update import EntityReportUpdate
from EntityReport.location_generator import LocationGenerator
from DetectionIdGenerator.detection_id_generator_uuid import DetectionIdGeneratorUUID
from Reporter.print_reporter import PrintReporter


if __name__ == "__main__":
    from report_generator import ReportGenerator

    location_generator = LocationGenerator()
    entity_report_factory = EntityReportFactory(DetectionIdGeneratorUUID(), location_generator)
    entity_report_update = EntityReportUpdate(location_generator)

    reporter = ReportGenerator(entity_report_factory, entity_report_update, 10, PrintReporter())
    reporter.generate()
