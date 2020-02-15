import random
###########Generates Random Board (Takes a number)################
def generate_queenboard(n):
  a = [[ 0 for i in range(n)]for j in range(n)]
  random.seed(2)
  for i in range(0,n):
    a[random.randrange(0,n-1)][i] = random.randrange(1,9)
  return a# returns an 2D array
######################################3

#######Prints the board takes 2d array as input#################
def print_board(board):
  for x in board:
    print(x)

#########Finds number or attacking queens (inputs board and returns array of attacking queens weights)
def find_no_of_attacking_queens(board):
  n = len(board)
  #print("Length",n)
  attack_queens =[]
  for x in range(0,n):
    #print("x",x)
    for y in range(0,n):
      #print("y",y)
      if(board[x][y]>0):
        #print("current",board[x][y])
        #finding queens on side - 
        row =x
        #print("row1",row)
        coloumn =y+1
        #print("col1",coloumn)
        while(coloumn<n):
          if(board[row][coloumn]>0):
            attack_queens.append([board[x][y],board[row][coloumn]])
            #print(board[x][y],board[row][coloumn])
          coloumn = coloumn+1
          #print("update col",coloumn)
        #print("board after first right pass",attack_queens)
        #finding queens on upper diagonal
        if(x!=0):
          row = x-1
          #print("row2",row)
          coloumn = y+1
          #print("col2",coloumn)
          while(0<row<n and coloumn<n):
            if(board[row][coloumn]>0):
              attack_queens.append([board[x][y],board[row][coloumn]])
            row = row-1
            coloumn = coloumn+1
        #print("board after second right pass",attack_queens)
        #finding queens on lower right diagonal
        row = x+1
        #print("row3",row)
        coloumn = y+1
        #print("row3",coloumn)
        while(row<n and coloumn<n):
          if(board[row][coloumn]>0):
            attack_queens.append([board[x][y],board[row][coloumn]])
          row = row+1
          #print("updated row",row)
          coloumn = coloumn+1
          #print("updated col",coloumn)
        #print("board after third right pass",attack_queens)
  return attack_queens
##################################################

##########Calculates the move cost###########
def move_cost(weight,dist):
  return(weight*dist)
####################################

############Takes a board and moves the queen at current position(row,col) to desired position (row,col)
def move_queen(board,curr_row,curr_col,des_row,des_col):
  board[des_row][des_col]=board[curr_row][curr_col]
  board[curr_row][curr_col] = 0
  return board;

#########################################################3

a =(generate_queenboard(6))
print_board(a)
print(find_no_of_attacking_queens(a))
