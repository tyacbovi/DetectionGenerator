import argparse


class DetectionGeneratorCLI:
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument("-f", "--reports-per-second", type=int, default=10,dest="freq",
                                 help="Overall number of reports this generator will create/update.")
        self.parser.add_argument("-b", "--brokers", type=str, default="localhost:9092", dest="brokers")
        self.parser.add_argument("-s", "--source-name", type=str, default="test", dest="source_name")
        self.parser.add_argument("-d", "--debug-lvl", type=str, default="INFO", dest="debug_lvl")
        self.parser.add_argument("-c", "--clear-all", type=bool, default=True, dest="to_clear")

    def get_user_settings(self):
        return self.parser.parse_args()

