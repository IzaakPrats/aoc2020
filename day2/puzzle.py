def parse(lines):
    def p(line):
        return {
            "least": line.split(' ')[0].split('-')[0],
            "most":  line.split(' ')[0].split('-')[1],
            "term": line.split(' ')[1][0],
            "password": line.split(' ')[2]
        }

    return map(p, lines)


def isValid(m, l, t, p):
    l = l
    m = m

    lMatch = False
    mMatch = False

    for i in range(0, len(p)):
        if (i == (m - 1) and p[i] == t):
            mMatch = True
        if (i == (l - 1) and p[i] == t):
            lMatch = True

    return (mMatch and not lMatch) or (lMatch and not mMatch)


def solve(data):
    count_valid = 0
    for d in data:
        most = int(d["most"])
        least = int(d["least"])
        term = d["term"]
        password = d["password"]

        if isValid(most, least, term, password):
            count_valid += 1

    return count_valid
