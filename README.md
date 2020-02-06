# Heavy-N-Queens
Addressing Heavy N-Queens Problem
Part 1.  Heavy N-queens problem
The problem
For this problem, you will work on a variant of the N-queens problem we discussed in class.  Some of the queen pieces are very heavy, and therefore difficult to move.  Queens have a weight ranging from 1 to 9 (integers).  The cost to move a queen is the number of tiles you move it times its weight.  So to move a queen weighing 6 upwards by 4 squares in a column costs 6 * 4 = 24.  

In addition, your program must work with a given starting board and find a low-cost solution.  In other words, if you use random restarts you may not rearrange the pieces on the board.  You are allowed to make different choices about which Queen to move on the restart.  

Otherwise, the rules are identical to the N-queens problem.  
Heuristics
For your search, you need a heuristic function.  The number of (directly and indirectly) attacking queens is a good place to start.  Each pair of attacking Queens requires moving one of them -- presumably the lightest.  You should look at each pair of attacking Queens, and select the lightest one to move.  Construct two heuristic functions:
H1.  The lightest Queen across all pairs of Queens attacking each other.  Moving that Queen is the minimum possible cost to solve the problem (in real life it will probably take more effort than that though).
H2.  Sum across every pair of attacking Queens the weight of the lightest Queen.

It is not immediately obvious that H2 is admissible.  Either prove that it is admissible or construct a counterexample to prove that it is not.  

Extra credit:  develop a heuristic H3 that is is better than H1 and is admissible.  Prove/demonstrate that H3 is admissible.  
Approaches
You will use two approaches for this problem:  A* and greedy hill climbing with restarts.  You are free to make use of sideways moves, first choice hill climbing, or simulated annealing.  You are not required to use any particular technique for deciding how to allocate your time.  However, your decisions should have empirical support.  In other words, you will need to present data for why (for example) you do first-choice hill climbing with at most 3 sideways moves.    

For hill climbing with restarts, you should use H1 and H2 and perform greedy hill climbing.  If you have not found a solution, and fewer than 10 seconds have elapsed since the program started running, you should do another iteration of hill climbing with the same start state (you may not change the initial configuration of Queens).  
Program behavior 
Your program should take as input the N value for the N-queens problem, the type of search to conduct (1 for A*, 2 for greedy hill climbing), and which heuristic to use (H1 or H2).  For example, passing in a “30 1 H2” results in attempting to solve a 30-queens puzzle with A* search using H2.  You can take input as command-line input, or read it from a file if command-line input is difficult for the language you are using.  Just explain how to invoke your program in your writeup.
  
Your program should output:
The start state (a simple text representation is fine)
The number of nodes expanded.  Consider an expansion as when you visit a node and compute the cost for all of the possible next moves.  For hill climbing, remember to count this value across all of the restarts!  
Time to solve the puzzle
The effective branching factor:  consider how many nodes were expanded vs. the length of the solution path
The cost to solve the puzzle.  Note that A* computes cost automatically, but you will need to extend greedy search to keep track of this number.  Note that cost does not include any failed runs with greedy search -- just compute the cost of the path it computes for the board it solves.  (Note the comparison with A* is not quite fair since greedy search gets to discard its results from tougher boards)
The sequence of moves needed to solve the puzzle, if any (hill climbing may fail).
Writeup
You should conduct experiments to determine:
How large of a puzzle can your program typically solve within 10 seconds using A*?  Using greedy hill climbing?
What is the effective branching factor?  For this computation, perform 10 runs of a puzzle half the maximum size you calculated for step #1.    
Compute the branching factor using H1 for A* and greedy search
Compute the branching factor using H2 for A* and greedy search
Which approach comes up with cheaper solution paths?  Why?
Which approach typically takes less time?  Why?
Either prove the heuristic for A* is admissible, or provide a counterexample demonstrating that it is not.
