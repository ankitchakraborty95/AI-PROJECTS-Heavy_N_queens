import math
import random
import numpy
import time
from common_functions import *
################################################################################

####################################################################################
def calc_full_h(h_value,board):
    heuristic_board=[[100000 for x in range(0,len(board))] for y in range(0,len(board))]
    for x in range(0,len(board)):
        for y in range(0,len(board)):
            if(board[x][y]>0):
                queen_row = x
                queen_col = y
                succ_row = x
                succ_col = y
                #print("queen row col",board[x][y],x,y)
                while(succ_row>0):
                    succ_row = succ_row-1
                    #print("successor row col",succ_row,succ_col)
                    succ_board = move_queen(board,queen_row,queen_col,succ_row,succ_col)
                    #print("succ board")
                    #print_board(succ_board)
                    succ_attack_pairs = find_no_of_attacking_queens(succ_board)
                    #print("attacking pair after moving",succ_attack_pairs)
                    succ_h_value = calc_h(h_value,succ_attack_pairs)
                    #print("succ h value", succ_h_value)
                    heuristic_board[succ_row][succ_col]=succ_h_value
                    #print_board(heuristic_board)
                #print("original board")
                succ_row = x
                succ_col = y
                while (succ_row <len(board)-1):
                    succ_row = succ_row +1
                    #print("successor row col", succ_row, succ_col)
                    succ_board = move_queen(board, queen_row, queen_col,succ_row,succ_col)
                    #print("succ board")
                    #print_board(succ_board)
                    succ_attack_pairs = find_no_of_attacking_queens(succ_board)
                    #print("attacking pair after moving", succ_attack_pairs)
                    succ_h_value = calc_h(h_value, succ_attack_pairs)
                    #print("succ h value", succ_h_value)
                    heuristic_board[succ_row][succ_col] = succ_h_value
                    #print_board(heuristic_board)
    #print("org board")
    #print_board(board)
    #print("h board")
    #print_board(heuristic_board)
    return(heuristic_board)


def hc_try(board,heuristic,sideway):
    sideways_move = sideway
    moves = 0
    nodes_expanded = 0
    total_move_cost = 0
    h_selected = heuristic
    input_board = board
    seq_of_moves = []
    current_board = [x for x in input_board]
    # print("current board")
    # print_board(current_board)
    # print("input board")
    # print_board(input_board)
    run_heuristic = True
    #########################################################################################
    while (run_heuristic):
        attack_pair = find_no_of_attacking_queens(current_board)
        # print(attack_pair)
        current_heuristic = calc_h(h_selected, attack_pair)
        # print("h1", current_heuristic)
        succ_h_board = calc_full_h(h_selected, current_board)
        nodes_expanded = nodes_expanded+1
        # print("nodes expanded",nodes_expanded)
        # print("succ h board")
        # print_board(succ_h_board)
        min_pos_h = numpy.min(succ_h_board)
        # print("min pos h", min_pos_h)
        if (min_pos_h == 0):
            # print("sol found")
            better_pos_row = 0
            better_pos_col = 0
            for x in range(0, len(succ_h_board)):
                for y in range(0, len(succ_h_board)):
                    if (min_pos_h == succ_h_board[x][y]):
                        better_pos_row = x
                        better_pos_col = y
            queen_current_pos_row = 0
            queen_current_pos_col = better_pos_col
            for x in range(0, len(current_board)):
                if (current_board[x][better_pos_col] > 0):
                    queen_current_pos_row = x
            # print("current queen pos", queen_current_pos_row, queen_current_pos_col)
            #print("desired queen pos ", "col ", better_pos_col, " row ", better_pos_row)
            seq_of_moves.append([better_pos_col,better_pos_row])
            total_move_cost = total_move_cost + move_cost(current_board[queen_current_pos_row][queen_current_pos_col],
                                                          queen_current_pos_row, better_pos_row)
            current_board = move_queen(current_board, queen_current_pos_row, queen_current_pos_col, better_pos_row,
                                       better_pos_col)
            moves = moves + 1
            return [current_board,total_move_cost,moves,nodes_expanded,seq_of_moves]
            # print("board after moving to better pos")
            # print_board(current_board)


        if (min_pos_h < current_heuristic):
            # print("better pos")
            better_pos_row = 0
            better_pos_col = 0
            for x in range(0, len(succ_h_board)):
                for y in range(0, len(succ_h_board)):
                    if (min_pos_h == succ_h_board[x][y]):
                        better_pos_row = x
                        better_pos_col = y
            queen_current_pos_row = 0
            queen_current_pos_col = better_pos_col
            for x in range(0, len(current_board)):
                if (current_board[x][better_pos_col] > 0):
                    queen_current_pos_row = x
            # print("current queen pos", queen_current_pos_row, queen_current_pos_col)
            #print("desired queen pos", " col ", better_pos_col, " row ", better_pos_row)
            seq_of_moves.append([better_pos_col, better_pos_row])
            total_move_cost = total_move_cost + move_cost(current_board[queen_current_pos_row][queen_current_pos_col],
                                                          queen_current_pos_row, better_pos_row)
            current_board = move_queen(current_board, queen_current_pos_row, queen_current_pos_col, better_pos_row,
                                       better_pos_col)
            moves = moves + 1
            # print("board after moving to better pos")
            # print_board(current_board)



        elif (min_pos_h == current_heuristic):
            # print("sideway move")
            sideways_move = sideways_move - 1
            # print("sideway move no",sideways_move)
            if (sideways_move > 0):
                similar_pos_row = 0
                similar_pos_col = 0
                found = False
                while (found == False):
                    i = random.randrange(0, len(succ_h_board))
                    j = random.randrange(0, len(succ_h_board))
                    if (succ_h_board[i][j] == min_pos_h):
                        similar_pos_row = i
                        similar_pos_col = j
                        found = True

                queen_current_pos_row = 0
                queen_current_pos_col = similar_pos_col
                for x in range(0, len(current_board)):
                    if (current_board[x][similar_pos_col] > 0):
                        queen_current_pos_row = x
                # print("current queen pos", queen_current_pos_row, queen_current_pos_col)
                #print("desired queen pos", " col ", similar_pos_col, " row ", similar_pos_row)
                seq_of_moves.append([similar_pos_col, similar_pos_row])
                total_move_cost = total_move_cost + move_cost(
                    current_board[queen_current_pos_row][queen_current_pos_col],
                    queen_current_pos_row, similar_pos_row)
                current_board = move_queen(current_board, queen_current_pos_row, queen_current_pos_col, similar_pos_row,
                                           similar_pos_col)
                moves = moves + 1
                # print("board after moving to similar pos")
                # print_board(current_board)


            else:
                return [current_board, total_move_cost, moves,nodes_expanded]


        else:
            print("local min reached")
            return [current_board, total_move_cost, moves,nodes_expanded,seq_of_moves]


########################################################
def hc_restart(board_given,heuristic_given):
    start_time = time.perf_counter()
    input_board = board_given
    sideways_allowed = 12
    heuristic_selected = heuristic_given
    restart = True
    best_sol_board = 0
    best_no_of_moves = 0
    total_nodes_expanded = 0
    final_seq = []
    attack_queens = len(find_no_of_attacking_queens(input_board))
    while (restart):
        ans = hc_try(input_board, heuristic_selected, sideways_allowed)
        # print(ans)
        #print("solved" if (len(find_no_of_attacking_queens(ans[0])) == 0) else "unsolved")
        sol_found = True if (len(find_no_of_attacking_queens(ans[0])) == 0) else False
        if (sol_found):
            best_cost = ans[1]
            best_sol_board = ans[0]
            best_no_of_moves = ans[2]
            total_nodes_expanded = ans[3]+total_nodes_expanded
            final_seq = ans[4]
            restart = False
        else:
            if (len(find_no_of_attacking_queens(ans[0])) <= attack_queens):
                best_cost = ans[1]
                best_sol_board = ans[0]
                best_no_of_moves = ans[2]
                total_nodes_expanded = ans[3]+total_nodes_expanded
        end_time = time.perf_counter()
        execution_time = (end_time - start_time)
        if (execution_time >= 10):
            restart = False
            break

    print("Puzzle Solved after taking seq - [queen in col,to row]",final_seq if (len(find_no_of_attacking_queens(best_sol_board)) == 0) else "Puzzle unsolved")
    print("Final board after HC")
    print_board(best_sol_board)
    print("Solution cost", best_cost)
    print("no of moves", best_no_of_moves)
    print("total nodes expanded", total_nodes_expanded)
    print("branching factor",total_nodes_expanded/best_no_of_moves)
    end_time = time.perf_counter()
    execution_time = (end_time - start_time)
    print("execution time", execution_time)
