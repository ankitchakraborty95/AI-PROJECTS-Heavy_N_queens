from random_board_generator_function import generate_queenboard
from random_board_generator_function import print_board
from common_functions import *
import csv
import sys

# Generates a board with a random size
def rand_n_queens(alg, heuristic):
    random.seed(random.random())
    board = (generate_queenboard(random.randrange(5, 100)))
    print_board(board)
    k = find_no_of_attacking_queens(board)
    h = calc_h(heuristic, k)
    print(h)
    pass

# Generates a board with a specified size
def num_n_queens(num, alg, heuristic):
    board = (generate_queenboard(num))
    print_board(board)
    k = find_no_of_attacking_queens(board)
    h = calc_h(heuristic, k)
    print(h)
    pass

# Uses a given csv file
def n_queens(fname, alg, heuristic):
    board = read_board(fname)
    for x in board:
        print(x)
    k = find_no_of_attacking_queens(board)
    h = calc_h(heuristic, k)
    print(k)

def is_intstring (s):
    try:
        int(s)
        return True
    except ValueError:
        return False

if __name__ == "__main__":
    if len(sys.argv) == 3:
        rand_n_queens(sys.argv[1], sys.argv[2])
    elif len(sys.argv) == 4 and is_intstring(sys.argv[1]):
        num_n_queens(int(sys.argv[1]), sys.argv[2], sys.argv[3])
    elif len(sys.argv) == 4 and ~is_intstring(sys.argv[1]):
        n_queens(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        print("Ya got nothing")

