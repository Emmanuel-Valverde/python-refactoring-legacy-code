from report import Report


class ReportRepository:

    def __init__(self, report_file=None):
        self.report_file = report_file

    def get_all_reports(self):
        with open(self.report_file, "r") as file:
            reports = []
            for report in file:
                levels = list(map(int, report.split()))
                reports.append(Report(levels))

            return reports
