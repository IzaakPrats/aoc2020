def parse(lines):
    return map(lambda str: str.split('\n'),
               ''.join(lines).split('\n\n'))


def solve_first(data):
    group_sum = 0

    for group in data:
        charSet = set()
        for char in group:
            charSet.add(char)
        group_sum += len(charSet)

    return group_sum


def solve_second(data):
    group_sum = 0

    for group in data:
        agree = {}

        for person in group:
            for char in person:
                if agree.get(char) is None:
                    agree[char] = 1
                else:
                    agree[char] += 1

        for agree_key in agree:
            if agree[agree_key] == len(group):
                group_sum += 1

    return group_sum


def solve(data):
    return solve_second(data)
