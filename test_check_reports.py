import unittest
import io
from main import check_reports


class TestCheckReports(unittest.TestCase):
    def test_check_report(self):
        input_data = io.StringIO("""7 6 4 2 1
        1 2 7 8 9
        9 7 6 2 1
        1 3 2 4 5
        8 6 4 4 1
        1 3 6 7 9""")

        expected_output = 2
        result = check_reports(input_data)
        self.assertEqual(result, expected_output)

    def test_report_should_be_secure_when_level_decrease_one_or_two_levels(self):
        input_data = io.StringIO("""7 6 4 2 1""")
        expected_output = 1
        self.assertEqual(check_reports(input_data), expected_output)