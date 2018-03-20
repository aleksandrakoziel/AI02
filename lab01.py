import queen as q
import utils as u

queens1 = [q.Queen(1,2), q.Queen(2,4), q.Queen(3,6), q.Queen(4,1), q.Queen(5,6), q.Queen(6,5)]
print(u.is_solved_queens(queens1))

queens2 = [q.Queen(1,5), q.Queen(2,3), q.Queen(3,1), q.Queen(4,6), q.Queen(5,4), q.Queen(6,2)]
print(u.is_solved_queens(queens2))

queens3 = [q.Queen(1,2), q.Queen(2,3), q.Queen(3,4), q.Queen(4,5), q.Queen(5,6), q.Queen(6,1)]
print(u.is_solved_queens(queens3))