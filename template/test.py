import puzzle

data = puzzle.parse(file("input.txt").readlines())

first_answer = puzzle.solve_first(data)
print("FIRST PART ANSWER IS: ", first_answer)

second_answer = puzzle.solve_second(data)
print("SECOND PART ANSWER IS: ", second_answer)
