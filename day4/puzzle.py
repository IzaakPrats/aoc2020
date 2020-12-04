import re

EYE_COLORS = "amb blu brn gry grn hzl oth".split(" ")


def parse(lines):
    fmt_lines = map(lambda str: str.replace('\n', ' '),
                    ''.join(lines).split('\n\n'))

    data = []
    for line in fmt_lines:
        pspt = {}
        pieces = line.split(' ')

        for piece in pieces:
            key = piece.split(':')[0]
            value = piece.split(':')[1]
            pspt[key] = value

        data.append(pspt)

    return data


def solve(data):
    count_valid = 0

    for pspt in data:
        keys = pspt.keys()

        if (len(keys) == 8 or (len(keys) == 7 and 'cid' not in keys)):
            if (int(pspt["byr"]) < 1920 or int(pspt["byr"]) > 2002):
                continue

            if (int(pspt["iyr"]) < 2010 or int(pspt["iyr"]) > 2020):
                continue

            if (int(pspt["eyr"]) < 2020 or int(pspt["eyr"]) > 2030):
                continue

            # check height
            unit = pspt["hgt"][-2:]
            if (unit != 'cm' and unit != 'in'):
                continue

            if (unit == 'cm'):
                height = int(pspt["hgt"][:-2])
                if (height < 150 or height > 193):
                    continue

            if (unit == 'in'):
                height = int(pspt["hgt"][:-2])
                if (height < 59 or height > 76):
                    continue

            if (not re.match("^#[a-f0-9]{6}$", pspt["hcl"])):
                continue

            if (pspt["ecl"] not in EYE_COLORS):
                continue

            if (not re.match("^[0-9]{9}$", pspt["pid"])):
                continue

            count_valid += 1

    return count_valid
