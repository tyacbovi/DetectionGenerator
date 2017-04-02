if __name__ == "__main__":
    from ais_data_source import AISDataSource
    from flights_data_source import FlightsDataSource
    from DetectionGenerator.Reporter.kafka_reporter import KafkaReporter
    import json
    from DetectionGenerator.utils.logger_util import log
    from external_data_source_cli import ExternalDataSourceCLI
    from external_source_event_loop import event_loop

    cli = ExternalDataSourceCLI()
    settings = cli.get_user_settings()
    broker_list = settings.brokers
    debug_level = settings.debug_lvl

    log().setLevel(debug_level)
    log().info("Generator started with the following settings: " + json.dumps(vars(settings)))

    if settings.source:
        kafka_reporter = KafkaReporter(_kafka_broker_ip=broker_list, _topic="marine-traffic-raw-data", _sync_action=
        settings.kafka_sync)
        event_loop(reporter=kafka_reporter, data_source=AISDataSource())
    else:
        kafka_reporter = KafkaReporter(_kafka_broker_ip=broker_list, _topic="flight-radar-raw-data", _sync_action=
        settings.kafka_sync)
        event_loop(reporter=kafka_reporter, data_source=FlightsDataSource())
