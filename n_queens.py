from common_functions import *
from hc_with_restart import hc_restart
from aStar_call import *
import sys

# Generates a board with a random size
def rand_n_queens(alg, heuristic):
    print("alg selected",alg)
    print("heuristic selected",heuristic)
    board = (generate_queenboard(random.randrange(5,15)))
    print("start state")
    print_board(board)
    k = find_no_of_attacking_queens(board)
    h = calc_h(int(heuristic), k)
    print("attcking pair in input board", k)
    print("input board Heuristic",h)
    if alg == '2'or alg == 'HC':
        print("doing HC")
        hc_restart(board,int(heuristic))
    if alg == '1'or alg == 'A*':
        print('doing A*')
        aStar_call(board, int(heuristic))
    pass

# Generates a board with a specified size
def num_n_queens(num, alg, heuristic):
    print("number selected",num)
    print("alg selected", alg)
    print("heuristic selected",heuristic)
    board = (generate_queenboard(num))
    print("start state")
    print_board(board)
    k = find_no_of_attacking_queens(board)
    h = calc_h(int(heuristic), k)
    print("attcking pair in input board",k)
    print("input board Heuristic", h)
    if alg == '2'or alg == 'HC':
        print("doing HC")
        hc_restart(board,int(heuristic))
    if alg == '1'or alg == 'A*':
        print('doing A*')
        aStar_call(board, int(heuristic))
    pass

# Uses a given csv file
def n_queens(fname, alg, heuristic):
    print("alg selected", alg)
    print("heuristic selected", heuristic)
    board = read_board(fname)
    print("start state")
    print_board(board)
    k = find_no_of_attacking_queens(board)
    h = calc_h(int(heuristic),k)
    print("attcking pair in input board",k)
    print("input board Heuristic", h)
    if alg == '2' or alg == 'HC':
        print("doing HC")
        hc_restart(board,int(heuristic))
    if alg == '1'or alg == 'A*':
        print('doing A*')
        aStar_call(board, int(heuristic))


def is_intstring (s):
    try:
        int(s)
        return True
    except ValueError:
        return False

if __name__ == "__main__":
    if len(sys.argv) == 3:
        heuristic = 0
        if(sys.argv[2] == 'H1'):
            heuristic = 1
        if(sys.argv[2] == 'H2'):
            heuristic = 2
        rand_n_queens(sys.argv[1], heuristic)
    elif len(sys.argv) == 4 and is_intstring(sys.argv[1]):
        heuristic = 0
        if (sys.argv[3] == 'H1'):
            heuristic = 1
        if (sys.argv[3] == 'H2'):
            heuristic = 2
        num_n_queens(int(sys.argv[1]), sys.argv[2], heuristic)
    elif len(sys.argv) == 4 and is_intstring(sys.argv[1])!= True:
        heuristic = 0
        if (sys.argv[3] == 'H1'):
            heuristic = 1
        if (sys.argv[3] == 'H2'):
            heuristic = 2
        n_queens(sys.argv[1], sys.argv[2], heuristic)
    else:
        print("Ya got nothing")
