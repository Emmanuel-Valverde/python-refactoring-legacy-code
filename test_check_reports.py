import io

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

    def test_report_should_be_insecure_when_level_increase_five_levels(self):
        input_data = io.StringIO("""1 2 7 8 9""")
        expected_output = 0
        assert check_reports(input_data) == expected_output

    def test_report_should_be_insecure_when_level_decrease_four_levels(self):
        input_data = io.StringIO("""9 7 6 2 1""")
        expected_output = 0
        assert check_reports(input_data) == expected_output