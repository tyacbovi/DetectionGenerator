
if __name__ == "__main__":
    from EntityReport.entity_report_factory import EntityReportFactory
    from EntityReport.entity_report_update import EntityReportUpdate
    from EntityReport.location_generator import LocationGenerator
    from DetectionIdGenerator.detection_id_generator_uuid import DetectionIdGeneratorUUID
    from Reporter.kafka_reporter import KafkaReporter
    from report_generator import ReportGenerator
    from detetction_generator_cli import DetectionGeneratorCLI
    import plyvel
    from entities_manager import EntitiesManager

    location_generator = LocationGenerator()
    db_connection = plyvel.DB('/tmp/entities_pool/', create_if_missing=True)

    entity_report_factory = EntityReportFactory(DetectionIdGeneratorUUID(), location_generator)
    entity_report_update = EntityReportUpdate(location_generator)

    cli = DetectionGeneratorCLI()
    settings = cli.get_user_settings()
    number_of_updates_per_sec = settings.freq
    broker_list = settings.brokers
    source_name = settings.source_name

    kafka_reporter = KafkaReporter(_kafka_broker_ip=broker_list, _topic=source_name)
    entities_manager = EntitiesManager(db_connection, entity_report_factory, entity_report_update, source_name)

    reporter = ReportGenerator(entities_manager, number_of_updates_per_sec, kafka_reporter)
    while (True):
        reporter.generate()
