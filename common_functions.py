import random
import numpy
import csv

#########Finds number or attacking queens (inputs board and returns array of attacking queens weights)
def generate_queenboard(n):
  a = [[ 0 for i in range(n)]for j in range(n)]
  random.seed(random.random())
  for i in range(0,n):
    a[random.randrange(0,n-1)][i] = random.randrange(1,9)
  return a


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
def move_cost(weight,curr_row,move_row):
    return ((weight * weight * abs(curr_row-move_row)))


####################################
#######Prints the board takes 2d array as input#################
def print_board(board):
  for x in board:
    print(x)

############Takes a board and moves the queen at current position(row,col) to desired position (row,col)
def move_queen(board, curr_row, curr_col, des_row, des_col):
    if(curr_row==des_row and curr_col==des_col):
        return board
    copy_board = [[0 for x in range(0,len(board))]for y in range(0,len(board))]
    for x in range(0,len(board)):
        for y in range(0,len(board)):
            copy_board[x][y]=board[x][y]
    copy_board[des_row][des_col] = board[curr_row][curr_col]
    copy_board[curr_row][curr_col] = 0
    return copy_board


#########################################################3

#####Calculate heuristic based on input##############
####takes input 1 or 2 and list_pf_attacking_pairs########
def calc_h(number,list_attacking_queens):
  if(number==1):###3calc h1 min of attacking pairs
      if(len(list_attacking_queens)==0):
          return 0
      else:
          value = min(min(list_attacking_queens))
          return (value**2)
  elif(number==2):###3calc h2 sum of min of attacking pairs
    if (len(list_attacking_queens) == 0):
        return 0
    sum =0
    for x in list_attacking_queens:
      sum = sum + min(x)
    return(sum)
  else:######if invalid input exit the loop
    print("invalid input of heuristic")
    return 0

def read_board(filename):
  rows = []
  board = []
  i=0
  # Read the CSV file
  with open(filename, 'r', encoding='utf-8-sig') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
      rows.append(row)

  for row in rows:
    board.append([])
    for col in row:
      if col != '':
        board[i].append(int(col))
      else:
        board[i].append(0)
    i += 1
  return board
