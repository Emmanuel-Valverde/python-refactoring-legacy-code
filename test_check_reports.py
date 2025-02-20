import io
from unittest.mock import patch

import pytest

from main import check_reports
from report import Report
from report_repository import ReportRepository


class TestCheckReports:

    def test_report_should_be_secure_when_level_decrease_one_or_two_levels(self):
        input_data = io.StringIO("""7 6 4 2 1""")
        expected_output = 1

        with patch.object(ReportRepository, 'get_all_reports', return_value=[Report([7,6,4,2,1])]):
            assert check_reports(ReportRepository()) == expected_output

    def test_secure_report_when_the_level_increases_between_the_boundaries(self):
        input_data = io.StringIO("""1 3 6 7 9""")
        expected_output = 1

        with patch.object(ReportRepository, 'get_all_reports', return_value=[Report([1, 3, 6, 7, 9])]):
            assert check_reports(ReportRepository()) == expected_output

    @pytest.mark.parametrize("report_input, expected, report", [
        ("1 2 7 8 9", 0, [Report([1, 2, 7, 8, 9])]),
        ("9 7 6 2 1", 0, [Report([9, 7, 6, 2, 1])])
    ])
    def test_insecure_reports_when_the_increase_or_decrease_is_out_of_bound(self, report_input, expected, report):
        report_file = io.StringIO(report_input)

        with patch.object(ReportRepository, 'get_all_reports', return_value=report):
            assert check_reports(ReportRepository()) == expected

    def test_insecure_report_when_the_levels_increase_and_decrease_in_the_same_report(self):
        input_data = io.StringIO("""1 3 2 4 5""")
        expected_output = 0

        with patch.object(ReportRepository, 'get_all_reports', return_value=[Report([1, 3, 2, 4, 5])]):
            repo = ReportRepository()
            assert check_reports(ReportRepository()) == expected_output

    def test_insecure_report_when_the_levels_do_not_increase_or_decrease(self):
        input_data = io.StringIO("""8 6 4 4 1""")
        expected_output = 0

        with patch.object(ReportRepository, 'get_all_reports', return_value=[Report([8, 6, 4, 4, 1])]):
            assert check_reports(ReportRepository()) == expected_output