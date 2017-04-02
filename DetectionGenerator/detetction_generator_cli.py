import argparse


class DetectionGeneratorCLI:
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument("-f", "--reports-per-second", type=int, default=1, dest="freq",
                                 help="Frequency of reporting each entity.")
        self.parser.add_argument("-n", "--number-of-entities", type=int, default=10, dest="number_of_entities",
                                 help="Overall number of entities this generator maintain.")
        self.parser.add_argument("-b", "--brokers", type=str, default="localhost:9092", dest="brokers")
        self.parser.add_argument("-s", "--source-name", type=str, default="test", dest="source_name")
        self.parser.add_argument("-d", "--debug-lvl", type=str, default="INFO", dest="debug_lvl")
        self.parser.add_argument("-c", "--clear-all", type=bool, default=False, dest="to_clear")
        self.parser.add_argument("-t", "--only-create", type=bool, default=False, dest="to_only_create",
                                 help="If on, will only create the entities")
        self.parser.add_argument("-w", "--wait-for-kafka-sync", type=bool, default=False, dest="kafka_sync",
                                 help="If on, will write and await to kafka")

    def get_user_settings(self):
        return self.parser.parse_args()
