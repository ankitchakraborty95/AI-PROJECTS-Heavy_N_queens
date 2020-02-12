import random
import numpy

class node():
  def __init__(self,row=0,col=0,weight=0):
    self.row = row
    self.col = col
    self.weight = 0
  def print_node(self):
    print("row",self.row)
    print("col",self.coloumn)
    print("weight",self.weight)
class board(node):
  def __init__(self,n):
    self.board = [[node() for j in range(n)] for i in range(n)]
    i=0
    j=0  
    for x in self.board:
      for y in x:
        y.row = i
        y.col =j
        j=j+1
      i=i+1
    random.seed(100)
    for x in range(n):
      (self.board[random.randrange(0,n)][x]).weight = random.randrange(1,10)

  def print_board(self):
    for x in self.board:
      for y in x:
        print([y.row,y.col,y.weight],"\t\t",end="")
      print("\n")

k = board(5)
k.print_board()