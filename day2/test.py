import puzzle


def main():
    data = puzzle.parse(file("input.txt").readlines())
    answer = puzzle.solve(data)
    print("ANSWER IS: ", answer)


if __name__ == '__main__':
    main()
