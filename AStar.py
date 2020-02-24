import numpy as np
import copy
import queue
import csv
import time
import random

class Queen:
    def __init__(self, x, y, weight):
        self.x = x
        self.y = y
        self.weight = weight

    def getCost(self, queen):
        """ Return cost between two queens according to heuristic
        Cost is 0 if queens do not collide
        """
        if self.x == queen.x or self.y == queen.y or ((self.x + self.y) == (queen.x + queen.y)) or (abs(self.x - self.y) == abs(queen.x - queen.y)):
            return min(self.weight, queen.weight)
        return 0

class Node:
    def __init__(self, state, cost_from_root, heuristic, level):
        self.state = state
        self.cost_from_root = cost_from_root
        self.n = len(self.state)
        self.heuristic = heuristic
        self.cost_to_goal = self.findCost() if heuristic == 1 else self.heuristic2()
        # print(self.cost_to_goal)
        self.total_cost = self.cost_from_root + self.cost_to_goal
        self.level = level
        self.path = []
        

    def findCost(self):
        cost = float("inf")
        num_attacking = 0
        for i in range(self.n - 1):
            for j in range(i + 1, self.n):
                c = self.state[i].getCost(self.state[j])
                # print(c, i, j, self.state[i].x, self.state[i].y, self.state[j].x, self.state[j].y)
                if c == 0:
                    continue
                else:
                    cost = min(cost, c)
                    num_attacking += 1
        return cost if num_attacking != 0 else 0

    def heuristic2(self):
        sumh = 0
        l = len(self.state)
        cost = float("inf")
        num_attacking = 0
        for i in range(l - 1):
            for j in range(i + 1, l):
                c = self.state[i].getCost(self.state[j])
                sumh = sumh + c

        return sumh

    def getNeighbours(self):
        neighbours = []
        for i in range(self.n):
            state = copy.deepcopy(self.state)
            queen = copy.deepcopy(state[i])
            for _ in range(self.n - 1):
                queen.x += 1
                queen.x %= self.n
                state[i] = queen
                cost_from_root = self.cost_from_root + queen.weight * abs(self.state[i].x - queen.x)
                neighbours.append(Node(copy.deepcopy(state), cost_from_root, self.heuristic, self.level + 1))
                neighbours[-1].path = self.path + [self]
        return neighbours

    def checkGoal(self):
        return self.cost_to_goal == 0
    def printNode(self):
        # print(self.total_cost, [queen.x for queen in self.state], [queen.weight for queen in self.state])
        board = np.zeros((self.n, self.n))
        for i in range(self.n):
            queen = self.state[i]
            board[i, queen.x] = queen.weight
        board = board.T
        print('Board : \n', board)
        print('Total Cost : ', self.total_cost)

    def __lt__(self, n):
        return self.total_cost < n.total_cost

    def printPath(self):
        for node in self.path:
            node.printNode()
        self.printNode()


class Graph:
    def __init__(self, board, heuristic):
        self.heuristic = heuristic
        self.n = len(board)
        self.start_node = self.boardToState(board)
        print('\n Start : ')
        self.start_node.printNode()
        self.expansions = 0


    def boardToState(self, board):
        board = np.array(board).T
        state = []
        for i in range(self.n):
            for j in range(self.n):
                if board[i][j] != 0:
                    state.append(Queen(j, i, board[i][j]))
        return Node(state, 0, self.heuristic, 0)

    # def getInitialConfig(self):
    #     weights = np.random.choice(9, size = self.n, replace = False)
    #     # weights = [1, 2, 3, 4, 5]
    #     weights = [i + 1 for i in weights]
    #     # states = [0, 0, 0, 0, 0]
    #     state = [Queen(np.random.randint(self.n), i, weights[i]) for i in range(self.n)]
    #     # state = [Queen(states[i], i, weights[i]) for i in range(self.n)]
    #     return Node(state, 0)

    def aStar(self):
        q = queue.PriorityQueue()
        visited = {}
        q.put(self.start_node)
        state = tuple([queen.x for queen in self.start_node.state])
        visited[state] = self.start_node
        start = time.time()
        while not q.empty():
            node = q.get()
            if time.time() - start > 10:
                return node
            
            # print(node.total_cost)
            # state = tuple([queen.x for queen in node.state])
            # node.printNode()
            # print(node.total_cost, node.cost_to_goal, node.cost_from_root)
            if node.checkGoal():
                return node
            neighbours = node.getNeighbours()
            # print('\n')
            for neighbour in neighbours:
                # neighbour.printNode()
                state = tuple([queen.x for queen in neighbour.state])
                if state in visited:
                    next_node = visited[state]
                    if neighbour.cost_from_root > next_node.cost_from_root:
                        continue
                else:
                    visited[state] = neighbour
                    self.expansions += 1
                    q.put(neighbour)
            # exit()    
        return None

# def read_board(filename):
#     rows = []
#     board = []
#     i=0
#     # print("Im here")
#     # Read the CSV file
#     with open(filename, 'r', encoding='utf-8-sig') as csvfile:
#         csvreader = csv.reader(csvfile)
#         for row in csvreader:
#             rows.append(row)

#     for row in rows:
#         board.append([])
#         for col in row:
#             if col != '':
#                 board[i].append(int(col))
#             else:
#                 board[i].append(0)
#         i += 1
#     return board
def generate_queenboard(n):
    a = [[ 0 for i in range(n)]for j in range(n)]
    for i in range(0,n):
        a[random.randrange(0,n-1)][i] = random.randrange(1,9)
    return a# returns an 2D array

def aStar_call(board,heuristic):
    start = time.time()
    restart = True
    graph = Graph(board, heuristic)
    # while(restart):
    goal = graph.aStar()
    assert goal is not None
    print('\n Path : ')
    goal.printPath()
    print('\n Goal/ solved board after a star : ')
    goal.printNode()
    print('\n Expansions : ', graph.expansions)
    print('Number of moves : ', goal.level)
    restart = False
    time_total = time.time() - start
    print('\n time taken to solve ',time_total)
    # else:
    #     print('\n Path : ')
    #     goal.printPath()
    #     print('\n Goal : ')
    #     goal.printNode()
    #     print('\n Expansions : ', graph.expansions)
    #     print('Length of path : ', goal.level)
    #     time_total = time.time() - start
        # if(time_total>=10):
        #     print('time exceeded')
        #     # restart = False
        #     print('\n Path : ')
        #     goal.printPath()
        #     print('\n Goal : ')
        #     goal.printNode()
        #     print('\n Expansions : ', graph.expansions)
        #     print('Length of path : ', goal.level)
            # break

    
            # print(time_total)
        



