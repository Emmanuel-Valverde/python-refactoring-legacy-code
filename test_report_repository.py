from report import Report
from report_repository import ReportRepository


class TestReportRepositoryShould:

    def test_get_reports(self):
        report_repository = ReportRepository("input_fixture.txt")
        expected_reports = [
            Report([7, 6, 4, 2, 1]),
            Report([1, 2, 7, 8, 9]),
            Report([9, 7, 6, 2, 1]),
            Report([1, 3, 2, 4, 5]),
            Report([8, 6, 4, 4, 1]),
            Report([1, 3, 6, 7, 9])
        ]

        assert expected_reports == report_repository.get_all_reports()
