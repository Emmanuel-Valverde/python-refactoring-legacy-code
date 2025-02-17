class Report:
    def __init__(self, report_data):
        self.report_data = report_data

    def is_safe(self):
        for index in range(len(self.report_data) - 1):

            next_level = self.report_data[index + 1]
            current_level = self.report_data[index]
            difference = next_level - current_level

            if self._is_increasing() and difference < 0:
                return False

            is_in_bounds = 0 < abs(difference) < 4

            if not is_in_bounds:
                return False

        return True

    def _is_increasing(self):
        if self.report_data[0] > self.report_data[1]:
            return False

        if self.report_data[0] < self.report_data[1]:
            return True

    def __eq__(self, other):
        if isinstance(other, Report):
            return self.report_data == other.report_data
        return False