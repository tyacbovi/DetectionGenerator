import argparse


class ExternalDataSourceCLI:
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument("-b", "--brokers", type=str, default="localhost:9092", dest="brokers")
        self.parser.add_argument("-d", "--debug-lvl", type=str, default="INFO", dest="debug_lvl")
        self.parser.add_argument("-s", "--source", type=bool, default=True, dest="source",
                                 help="Assign True for marinetraffic and False for flights")
        self.parser.add_argument("-w", "--wait-for-kafka-sync", type=bool, default=False, dest="kafka_sync",
                                 help="If on, will write and await to kafka")

    def get_user_settings(self):
        return self.parser.parse_args()
