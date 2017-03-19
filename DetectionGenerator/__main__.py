
if __name__ == "__main__":
    from EntityReport.entity_report_factory import EntityReportFactory
    from EntityReport.entity_report_update import EntityReportUpdate
    from EntityReport.location_generator import LocationGenerator
    from DetectionIdGenerator.detection_id_generator_uuid import DetectionIdGeneratorUUID
    from Reporter.print_reporter import PrintReporter
    from report_generator import ReportGenerator
    from detetction_generator_cli import DetectionGeneratorCLI

    location_generator = LocationGenerator()
    entity_report_factory = EntityReportFactory(DetectionIdGeneratorUUID(), location_generator)
    entity_report_update = EntityReportUpdate(location_generator)

    cli = DetectionGeneratorCLI()
    number_of_updates_per_sec = cli.get_user_settings().freq

    reporter = ReportGenerator(entity_report_factory, entity_report_update, number_of_updates_per_sec, PrintReporter())
    reporter.generate()
