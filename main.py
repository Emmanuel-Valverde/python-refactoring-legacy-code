from report_repository import ReportRepository


def check_reports(report_repository: ReportRepository):
    count = 0
    reports = report_repository.get_all_reports()

    for report in reports:
        if report.is_safe():
            count += 1
    return count



if __name__ == "__main__":
        print(check_reports(ReportRepository("input.txt")))