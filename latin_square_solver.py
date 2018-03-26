import random
import copy


class Square:
    def __init__(self, n):
        self.n = n
        self.n2 = n * n
        self.square = [None] * n * n
        self.options_available = []
        self.used_values = [None] * n * n
        self.set_of_numbers = list(range(1, n + 1))

    def latin_square_forward_checking_solver(self):

        for index in range(0, self.n2):
            self.options_available.append(copy.copy(self.set_of_numbers))

        self.square[0] = random.randint(1, self.n)
        self.used_values[0] = self.square[0]

        for position_row in range(0, self.n):
            self.options_available[position_row].remove(self.square[0])

        position_column = self.n
        while position_column < self.n2:
            self.options_available[position_column].remove(self.square[0])
            position_column += self.n

        position = 1
        while position < self.n2:
            if len(self.options_available[position]) > 0:
                self.square[position] = self.options_available[position][0]
                self.options_available[position].remove(self.square[position])
                self.used_values[position] = self.square[position]

                # remove the value from the future positions in the same column
                position_column = position + self.n
                while position_column < self.n2:
                    if self.square[position] in self.options_available[position_column]:
                        self.options_available[position_column].remove(self.square[position])
                    position_column += self.n

                # remove the value from the future positions in the same row
                positions_left_in_row = self.n - (position + 1) % self.n
                if positions_left_in_row != self.n:
                    position_row = 0
                    while positions_left_in_row > position_row:
                        position_row += 1
                        if self.square[position] in self.options_available[position + position_row]:
                            self.options_available[position + position_row].remove(self.square[position])

                position += 1

            else:
                position -= 1

                position_column = position + self.n
                while position_column < self.n2:
                    if self.square[position] not in self.options_available[position_column]:
                        self.options_available[position_column].append(self.square[position])

                    position_column += self.n

                # remove the value from the future positions in the same row
                positions_left_in_row = self.n - (position + 1) % self.n
                position_row = 0
                while positions_left_in_row > position_row:
                    position_row += 1
                    if self.square[position] not in self.options_available[position + position_row]:
                        self.options_available[position + position_row].append(self.square[position])

                self.fixing(position)

    def fixing(self, position):
        for index in range(0, position):
            self.remove_from_row(self.options_available, index, self.square[index])
            self.remove_from_column(self.options_available, index, self.square[index])

    def remove_from_row(self, options_available, position, value):
        # remove the value from the future positions in the same row
        positions_left_in_row = self.n - (position + 1) % self.n
        position_row = 1
        while positions_left_in_row < position_row:
            if value in options_available[position + position_row]:
                options_available[position + position_row].remove(value)
            position_row += 1

    def remove_from_column(self, options_available, position, value):
        # remove the value from the future positions in the same column
        position_column = position + self.n
        while position_column < self.n2:
            if value in options_available[position_column]:
                options_available[position_column].remove(value)
            position_column += self.n

    def latin_square_back_tracking_solver(self):

        for index in range(0, self.n2):
            self.options_available.append(copy.copy(self.set_of_numbers))

        self.square = []
        self.square.append(random.randint(1, self.n))

        position = 1
        while position < self.n2:
            if len(self.options_available[position]) > 0:
                current_value = random.choice(self.options_available[position])
                self.square.append(current_value)
                self.options_available[position].remove(current_value)

                if self.control_backward(position):
                    position += 1
                else:
                    self.square.pop()
            else:
                self.options_available[position] = (copy.copy(self.set_of_numbers))
                self.square.pop()
                position -= 1

    def control_backward(self, position):
        c = 0
        while c < position:
            row = set()
            r = 0
            while r < self.n and c + r <= position:
                row.add(self.square[c + r])
                r += 1

            if int(len(row)) != r:
                return False
            c += self.n

        for r in range(0, self.n):
            column = set()
            c = 0
            count_rows = 0
            while c < len(self.square) and c + r <= position:
                column.add(self.square[c + r])

                c += self.n
                count_rows += 1
            if len(column) != count_rows:
                return False

        return True

    def print_square(self):
        c = 0
        while c < len(self.square):
            print("| ", end=" ")
            for r in range(0, self.n):
                print(str(self.square[c + r]) + " | ", end=" ")
            c += self.n
            print("\n", end="")

    def is_valid(self):
        c = 0
        while c < len(self.square):
            row = set()
            for r in range(0, self.n):
                row.add(self.square[c + r])
            if len(row) != self.n:
                return False
            c += self.n

        for r in range(0, self.n):
            column = set()
            c = 0
            while c < len(self.square):
                column.add(self.square[c + r])
                c += self.n
            if len(column) != self.n:
                return False
        return True


# square = Square(2)
# square.latin_square_forward_checking_solver()
# print(square.square)

square3 = Square(9)
square3.latin_square_forward_checking_solver()
square3.print_square()
print(square3.is_valid())

square1 = Square(9)
square1.latin_square_back_tracking_solver()
square1.print_square()
print(square1.is_valid())
