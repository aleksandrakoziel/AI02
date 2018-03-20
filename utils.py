BOARD_SIZE = 6


# def under_attack(col, queens):
#     return col in queens or \
#            any(abs(col - x) == len(queens) - i for i, x in enumerate(queens))
#
#
# def solve(n):
#     solutions = [[]]
#     for row in range(n):
#         solutions = (solution + [i + 1]
#                      for solution in solutions  # first for clause is evaluated immediately,
#                      # so "solutions" is correctly captured
#                      for i in range(BOARD_SIZE)
#                      if not under_attack(i + 1, solution))
#     return solutions
#
#
# answers = solve(BOARD_SIZE)
# first_answer = next(answers)
# print(list(enumerate(first_answer, start=1)))
#

def is_solved_queens(queens):
    size = len(queens)
    x = []
    y = []

    # check if there is more than one
    # queen in the straight lines
    for q in queens:
        print("(" + str(q.x) + ", " + str(q.y) + ")")
        x.append(q.x)
        y.append(q.y)

    x = set(x)
    y = set(y)
    if (len(x) != size or len(y) != size):
        return False

    for q in queens:
        b1 = q.y - q.x
        b2 = q.y + q.x
        bum = 0
        for q in queens:
            if (q.y - q.x == b1 or q.y + q.x == b2):
                bum += 1
        if bum > 1:
            return False

    return True
