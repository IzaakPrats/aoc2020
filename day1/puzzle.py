def parse(lines):
    return map(lambda line: int(line), lines)


def solve(data):
    for n in range(0, len(data)):
        for m in range(0, len(data)):
            for j in range(0, len(data)):

                nNum = data[n]
                mNum = data[m]
                jNum = data[j]
                s = nNum + mNum + jNum

                if (s == 2020):
                    print(nNum * mNum * jNum)
    return -1
