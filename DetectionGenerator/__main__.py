
if __name__ == "__main__":
    from EntityReport.entity_report_factory import EntityReportFactory
    from EntityReport.entity_report_update import EntityReportUpdate
    from EntityReport.location_generator import LocationGenerator
    from DetectionIdGenerator.detection_id_generator_uuid import DetectionIdGeneratorUUID
    from Reporter.kafka_reporter import KafkaReporter
    from report_generator import ReportGenerator
    from detetction_generator_cli import DetectionGeneratorCLI

    location_generator = LocationGenerator()
    entity_report_factory = EntityReportFactory(DetectionIdGeneratorUUID(), location_generator)
    entity_report_update = EntityReportUpdate(location_generator)

    cli = DetectionGeneratorCLI()
    settings = cli.get_user_settings()
    number_of_updates_per_sec = settings.freq
    broker_list = settings.brokers
    source_name = settings.sorce_name

    kafka_reporter = KafkaReporter(_kafka_broker_ip=broker_list, _topic=source_name)

    reporter = ReportGenerator(entity_report_factory, entity_report_update, number_of_updates_per_sec, kafka_reporter)
    reporter.generate()
