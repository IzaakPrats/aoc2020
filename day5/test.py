import puzzle

data = puzzle.parse(file("input.txt").readlines())
answer = puzzle.solve(data)
print("ANSWER IS: ", answer)
