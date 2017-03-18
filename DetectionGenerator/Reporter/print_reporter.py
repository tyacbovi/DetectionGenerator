from reporter import Reporter


class PrintReporter(Reporter):
    def report(self, *args):
        print args
