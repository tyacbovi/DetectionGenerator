
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
    import json
    from utils.logger_util import log

    cli = DetectionGeneratorCLI()
    settings = cli.get_user_settings()

    number_of_updates_per_sec = settings.freq
    broker_list = settings.brokers
    source_name = settings.source_name
    debug_level = settings.debug_lvl
    to_empty_db = settings.to_clear

    log().setLevel(debug_level)
    log().info("Generator started with the following settings: " + json.dumps(vars(settings)))

    db_connection_name = '/tmp/entities_reports/'

    def db_setup():
        if to_empty_db:
            plyvel.destroy_db(db_connection_name)
        return plyvel.DB(db_connection_name, create_if_missing=True)

    db_connection = db_setup()

    location_generator = LocationGenerator()
    entity_report_factory = EntityReportFactory(DetectionIdGeneratorUUID(), location_generator)
    entity_report_update = EntityReportUpdate(location_generator)

    kafka_reporter = KafkaReporter(_kafka_broker_ip=broker_list, _topic=source_name + "-raw-data")
    entities_manager = EntitiesManager(db_connection, entity_report_factory, entity_report_update, source_name)

    reporter = ReportGenerator(entities_manager, number_of_updates_per_sec, kafka_reporter)

    if settings.to_only_create:
        reporter.generate()
        while True:
            import time
            time.sleep(1)
    else:
        while True:
            reporter.generate()
