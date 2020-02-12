import random
import numpy
###########Generates Random Board (Takes a number)################
def generate_queenboard(n):
  a = [[ 0 for i in range(n)]for j in range(n)]
  random.seed(2)
  for i in range(0,n):
    a[random.randrange(0,n-1)][i] = random.randrange(1,9)
  return a# returns an 2D array
######################################

#######Prints the board takes 2d array as input#################
def print_board(board):
  for x in board:
    print(x)