BOARD_SIZE = 6
import random


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


def is_solved_latin_square(squares):
    size = len(squares)

    for i in (0, size):
        row = squares[i]
        row = set(row)
        if (len(row) < size):
            return False
        column = []

        for j in (0, size):
            column.append(squares[i][j])

        column = set(column)
        if (len(column) < size):
            return False

    return True


def latin_square_forward_checking_solver(self, n):
    square = []
    options_available = []
    used_values = []

    set_of_numbers = list(range(1, n + 1))

    for position in range(0, n * n):
        options_available[position].append(set_of_numbers)

    square[0] = random.randint(1, n + 1)
    used_values[0] = square[0]

    for position_row in range(0, n):
        options_available[position_row].remove(square[0])

    position_column = n

    while position_column < n * n:
        options_available[position_column].remove(square[0])
        position_column + n

    position = 1

    while position < n * n:
        if len(options_available[position]) > 0:
            square[position] = options_available[position][0]
            options_available.remove(square[position])
            used_values[position] = square[position]

            # remove the value from the future positions in the same column
            position_column = position
            while position_column < n * n:
                if square[position] in options_available[position_column]:
                    options_available[position_column].remove(square[position])
                position_column += n

            # remove the value from the future positions in the same row
            positions_left_in_row = n - (position + 1) % n
            position_row = 1
            while positions_left_in_row < position_row:
                if square[position] in options_available[position + position_row]:
                    options_available[position + position_row].remove(square[position])
                position_row += 1

        else:
            return False

    return square

def remove_from_row(n, options_available, position, value):

    # remove the value from the future positions in the same row
    positions_left_in_row = n - (position + 1) % n
    position_row = 1
    while positions_left_in_row < position_row:
        if value in options_available[position + position_row]:
            options_available[position + position_row].remove(value)
        position_row += 1
