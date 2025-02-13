import io

import pytest

from main import check_reports


class TestCheckReports:
    def test_check_report(self):
        input_data = io.StringIO("""7 6 4 2 1
        1 2 7 8 9
        9 7 6 2 1
        1 3 2 4 5
        8 6 4 4 1
        1 3 6 7 9""")

        expected_output = 2
        result = check_reports(input_data)
        assert result == expected_output

    def test_report_should_be_secure_when_level_decrease_one_or_two_levels(self):
        input_data = io.StringIO("""7 6 4 2 1""")
        expected_output = 1
        assert check_reports(input_data) == expected_output

    def test_secure_report_when_the_level_increases_between_the_boundaries(self):
        input_data = io.StringIO("""1 3 6 7 9""")
        expected_output = 1
        assert check_reports(input_data) == expected_output

    @pytest.mark.parametrize("report, expected", [
        ("1 2 7 8 9", 0),
        ("9 7 6 2 1", 0)
    ])
    def test_insecure_reports_when_the_increase_or_decrease_is_out_of_bound(self, report, expected):
        report_file = io.StringIO(report)
        assert check_reports(report_file) == expected

    def test_insecure_report_when_the_levels_increase_and_decrease_in_the_same_report(self):
        input_data = io.StringIO("""1 3 2 4 5""")
        expected_output = 0
        assert check_reports(input_data) == expected_output

    def test_insecure_report_when_the_levels_do_not_increase_or_decrease(self):
        input_data = io.StringIO("""8 6 4 4 1""")
        expected_output = 0
        assert check_reports(input_data) == expected_output