from reporter import Reporter
from confluent_kafka import Producer
from DetectionGenerator.utils.logger_util import log


class KafkaReporter(Reporter):
    def __init__(self, _kafka_broker_ip, _topic, _sync_action = False):
        assert isinstance(_kafka_broker_ip, str)
        self.kafka_broker_ip = _kafka_broker_ip

        conf = {'bootstrap.servers': self.kafka_broker_ip}
        self.producer = Producer(conf)
        self.topic = _topic
        self.sync_action = _sync_action

    # Optional per-message delivery callback (triggered by poll() or flush())
    # when a message has been successfully delivered or permanently
    # failed delivery (after retries).
    @staticmethod
    def delivery_callback(err, msg):
        if err:
            log().error('%% Message failed delivery: %s\n' % err)
        else:
            log().debug('%% Message delivered to %s [%d]\n' % (msg.topic(), msg.partition()))

    def report(self, msg):
        try:
            self.producer.produce(self.topic, msg, callback=self.delivery_callback)

        except BufferError:
            log().error('%% Local producer queue is full '
                        '(%d messages awaiting delivery): try again\n' %
                        len(self.producer))
        if self.sync_action:
            self.producer.flush(timeout=500)
