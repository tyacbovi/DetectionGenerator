class ReportGenerator:
    def __init__(self, _number_of_reports, _report_func, _report_freq=1.0):
        self.number_of_reports = _number_of_reports
        self.report_freq = _report_freq
        self.report = _report_func

    def generate(self):
        for i in range(self.number_of_reports):
            self.report(i)
