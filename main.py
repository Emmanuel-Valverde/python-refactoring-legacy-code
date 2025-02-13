from io import StringIO


def check_reports(file: StringIO):
    count = 0
    for report in file:
        levels=list(map(int, report.split()))

        if levels[0] > levels[1]:
            increases = -1
        elif levels[0] < levels [1]:
            increases = 1
        else:
            continue

        if is_report_safe(increases, levels):
            count += 1
    return count


def is_report_safe(increases, levels):
    for index in range(len(levels) - 1):
        if 0 < (levels[index + 1] - levels[index]) * increases < 4:
            is_safe = True
        else:
            is_safe = False
            break
    return is_safe


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        print(check_reports(f))