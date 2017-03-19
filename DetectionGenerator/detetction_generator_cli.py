import argparse


class DetectionGeneratorCLI:
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument("-f", "--reports-per-second", type=int, default=10,dest="freq",
                                 help="Overall number of reports this generator will create/update.")

    def get_user_settings(self):
        return self.parser.parse_args()

