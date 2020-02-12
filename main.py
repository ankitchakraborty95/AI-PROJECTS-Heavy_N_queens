from random_board_generator_function import generate_queenboard
from random_board_generator_function import print_board
from common_functions import find_no_of_attacking_queens
from common_functions import calc_h


a =(generate_queenboard(7))
print_board(a)
k = find_no_of_attacking_queens(a)
h = calc_h(1,k)
print(h)
