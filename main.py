from io import StringIO


def check_reports(file: StringIO):
    count = 0
    for report in file:
        j=list(map(int, report.split()))

        if j[0] > j[1]:
            m = -1
        elif j[0] < j [1]:
            m = 1
        else:
            continue

        for x in range(len(j) -1):
            if 0 < (j[x + 1] -j [x] ) * m < 4:
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