from io import StringIO

from report import Report


def check_reports(file: StringIO):
    count = 0
    for report in file:
        levels=list(map(int, report.split()))
        report = Report(levels)

        if report.is_safe():
            count += 1
    return count

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        print(check_reports(f))