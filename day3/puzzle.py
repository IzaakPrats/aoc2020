def parse(lines):
    return map(lambda x: x.split("\n")[0], lines)


def solve(data):
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    tree_product = 1

    for slope in slopes:
        slopeCol = slope[0]
        slopeRow = slope[1]

        posRow = 0
        posCol = 0

        tree_count = 0

        while posRow < len(data):
            if (data[posRow][posCol] == '#'):
                tree_count += 1

            # apply slope
            posCol += slopeCol
            posRow += slopeRow

            if (posCol >= len(data[0])):
                posCol = posCol % len(data[0])

        tree_product *= tree_count

    return tree_product
