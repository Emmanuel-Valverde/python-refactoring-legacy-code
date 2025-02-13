from io import StringIO


def check_reports(file: StringIO):
    count = 0
    for report in file:
        levels=list(map(int, report.split()))

        if levels[0] > levels[1]:
            m = -1
        elif levels[0] < levels [1]:
            m = 1
        else:
            continue

        for x in range(len(levels) -1):
            if 0 < (levels[x + 1] -levels [x] ) * m < 4:
                t = True
            else:
                t = False
                break

        if t:
            count += 1
    return count


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        print(check_reports(f))