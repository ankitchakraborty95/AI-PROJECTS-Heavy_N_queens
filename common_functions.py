import random
import numpy


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
            #print("update",row,coloumn)
            #print("board before appending 1",attack_queens)
            #print("appending",board[x][y],board[row][coloumn])
            attack_queens.append([board[x][y],board[row][coloumn]])
            #print("board after appending 1",attack_queens)
          coloumn = coloumn+1
          #print("update",row,coloumn)
        #print("board after first right pass",attack_queens)
        if(x!=0):
          row = x-1
          #print("row2",row)
          coloumn = y+1
          #print("col2",coloumn)
          while(0<row<n and coloumn<n):
            if(board[row][coloumn]>0):
              #print("board before appending 2",attack_queens)
              attack_queens.append([board[x][y],board[row][coloumn]])
              #print("board after appending 2",attack_queens)
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
            #print("board before appending 3",attack_queens)
            attack_queens.append([board[x][y],board[row][coloumn]])
            #print("board after appending 3",attack_queens)
          row = row+1
          #print("updated row",row)
          coloumn = coloumn+1
          #print("updated col",coloumn)
        #print("board after third right pass",attack_queens)
        
  return attack_queens
##################################################

##########Calculates the move cost###########
def move_cost(weight,dist, curr_cost):
  return((weight*weight*dist)+curr_cost)
####################################

############Takes a board and moves the queen at current position(row,col) to desired position (row,col)
def move_queen(board,curr_row,curr_col,des_row,des_col):
  board[des_row][des_col]=board[curr_row][curr_col]
  board[curr_row][curr_col] = 0
  return board;

#########################################################3

#####Calculate heuristic based on input##############
####takes input 1 or 2 and list_pf_attacking_pairs########
def calc_h(number,list_attacking_queens):
  if(number==1):###3calc h1 min of attacking pairs
    return(numpy.min(list_attacking_queens))
  elif(number==2):###3calc h2 sum of min of attacking pairs
    sum =0
    for x in list_attacking_queens:
      sum = sum + min(x)
    return(sum)
  else:######if invalid input exit the loop
    print("invalid input of heuristic")
    return 0;