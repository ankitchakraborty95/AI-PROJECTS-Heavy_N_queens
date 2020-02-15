import math
import chardet
import pandas as pd
import random
import numpy
import time


def queen_board_input():
    with open(r"H:\WPI\spring 20\AI\ASSIGNMENT 1\heavy queens board.csv", 'rb') as f:  # change path accordingly
        result = chardet.detect(f.read())  # to detect the encoding of csv file
    # change path accordingly
    df = pd.read_csv(r"H:\WPI\spring 20\AI\ASSIGNMENT 1\heavy queens board.csv", encoding=result['encoding'],error_bad_lines=False, sep=',', engine='python', header=None)
    n = len(df)
    a = [[0 for x in range(0,n)]for y in range(0,n)]
    #print(df)
    board = [[0 for x in range(0,n)] for y in range(0,n)]
    for i in range(0,n):
        for j in range(0,n):
            if(math.isnan(df[i][j])==False):
                a[j][i] = int(df[i][j])


    #for x in a:
        #print(x)
    return a


#########Finds number or attacking queens (inputs board and returns array of attacking queens weights)
def find_no_of_attacking_queens(board):
    n = len(board)
    # print("Length",n)
    attack_queens = []
    for x in range(0, n):
        for y in range(0, n):
            if (board[x][y] > 0):
                #print("current queen",board[x][y],x,y)
                # finding queens on side -
                row = x
                coloumn = y
                while (coloumn < n-1):
                  coloumn = coloumn+1
                  #print("update side attack",row,coloumn,"value",board[row][coloumn])
                  if (board[row][coloumn] > 0):
                    attack_queens.append([board[x][y], board[row][coloumn]])
                # print("board after first right pass",attack_queens)
                ####finding queen on upeer dia
                row = x
                coloumn = y
                while (0<row  and coloumn < n-1):
                  row = row - 1
                  coloumn = coloumn + 1
                  #print("update upper diag attack",row,coloumn,"value",board[row][coloumn])
                  if (board[row][coloumn] > 0):
                    attack_queens.append([board[x][y], board[row][coloumn]])
                # print("board after second right pass",attack_queens)
                # finding queens on lower right diagonal
                row = x
                coloumn = y
                while (row < n-1 and coloumn < n-1):
                  row = row + 1
                  coloumn = coloumn + 1
                  #print("update lower diag attack",row,coloumn,"value",board[row][coloumn])
                  if (board[row][coloumn] > 0):
                    attack_queens.append([board[x][y], board[row][coloumn]])
                # print("board after third right pass",attack_queens)

    return attack_queens

##################################################

##########Calculates the move cost###########
def move_cost(weight, dist, curr_cost):
    return ((weight * weight * dist) + curr_cost)


####################################
#######Prints the board takes 2d array as input#################
def print_board(board):
  for x in board:
    print(x)

############Takes a board and moves the queen at current position(row,col) to desired position (row,col)
def move_queen(board, curr_row, curr_col, des_row, des_col):
    copy_board = [[0 for x in range(0,len(board))]for y in range(0,len(board))]
    for x in range(0,len(board)):
        for y in range(0,len(board)):
            copy_board[x][y]=board[x][y]
    copy_board[des_row][des_col] = board[curr_row][curr_col]
    copy_board[curr_row][curr_col] = 0
    return copy_board;


#########################################################3

#####Calculate heuristic based on input##############
####takes input 1 or 2 and list_pf_attacking_pairs########
def calc_h(number, list_attacking_queens):
    if (number == 1):  ###3calc h1 min of attacking pairs
        return (numpy.min(list_attacking_queens)**2)
    elif (number == 2):  ###3calc h2 sum of min of attacking pairs
        sum = 0
        for x in list_attacking_queens:
            sum = sum + min(x)
        return (sum)
    else:  ######if invalid input exit the loop
        print("invalid input of heuristic")
        return 0
################################################################################

####################################################################################
def calc_full_h(board,curr_h):
    heuristic_board=[[curr_h for x in range(0,len(board))] for y in range(0,len(board))]
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
                    succ_h_value = calc_h(1,succ_attack_pairs)
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
                    succ_h_value = calc_h(1, succ_attack_pairs)
                    #print("succ h value", succ_h_value)
                    heuristic_board[succ_row][succ_col] = succ_h_value
                    #print_board(heuristic_board)
    #print("org board")
    #print_board(board)
    #print("h board")
    #print_board(heuristic_board)
    return(heuristic_board)





########################################################
start = time.process_time()
sideways_move =10
input_board = queen_board_input()
current_board = [x for x in input_board]
#print("current board")
#print_board(current_board)
print("input board")
print_board(input_board)
run_heuristic = True
#########################################################################################
while(run_heuristic):
    attack_pair = find_no_of_attacking_queens(current_board)
    print(attack_pair)
    current_heuristic = calc_h(1, attack_pair)
    print("h1", current_heuristic)
    succ_h_board = calc_full_h(current_board, current_heuristic)
    # print_board(succ_h_board)
    min_pos_h = numpy.min(succ_h_board)
    print("min pos h", min_pos_h)
    if(min_pos_h==0):
        run_heuristic=False
        break
    if (min_pos_h < current_heuristic):
        print("better pos")
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
        print("current queen pos", queen_current_pos_row, queen_current_pos_col)
        print("desired queen pos", better_pos_row, better_pos_col)
        current_board = move_queen(current_board, queen_current_pos_row, queen_current_pos_col, better_pos_row,
                                   better_pos_col)
        print("board after moving to better pos")
        print_board(current_board)
        end =(time.process_time() - start)
        if(end>3):
            run_heuristic =False

    elif (min_pos_h == current_heuristic):
        print("sideway move")
        sideways_move = sideways_move - 1
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
            print("current queen pos", queen_current_pos_row, queen_current_pos_col)
            print("desired queen pos", similar_pos_row, similar_pos_col)
            current_board = move_queen(current_board, queen_current_pos_row, queen_current_pos_col, similar_pos_row,
                                       similar_pos_col)
            print("board after moving to similar pos")
            print_board(current_board)
            end = (time.process_time() - start)
            if (end > 3):
                run_heuristic = False
        else:
            run_heuristic = False


    else:
        print("local min reached")
        run_heuristic =False

attack_pair = find_no_of_attacking_queens(current_board)
print(attack_pair)
current_heuristic = calc_h(1, attack_pair)
print("h1", current_heuristic)
succ_h_board = calc_full_h(current_board, current_heuristic)
# print_board(succ_h_board)
min_pos_h = numpy.min(succ_h_board)
print("min pos h", min_pos_h)





