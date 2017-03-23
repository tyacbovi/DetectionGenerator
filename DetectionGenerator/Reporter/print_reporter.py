from reporter import Reporter


class PrintReporter(Reporter):
    def report(self, msg):
        print (msg)
