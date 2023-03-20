# Local Search and Optimization

## Solve the N-Queens problem by reducing it to an optimization problem and solving the same using local search algorithm

Given to you as attachments are two files - search.py and utils.py. In search.py, there is an implementation of an abstract class 'Problem' and an implementation of the class 'Node'. These classes provide generic interfaces to represent an AI search problem and a node in the search-space respectively. Additionally, the file also provides an implementation of the hill-climbing algorithm. The utils.py file implements a number of utility methods, some of which are used in search.py.

In particular, you have the following tasks:

1. Implement a sub-class of 'Problem' (say nQueens), with concrete implementation(s) of the methods required.
2. Modify the necessary methods in the Node class. Try minimal modification.
3. Modify/Use the hill-climbing algorithm to solve the N-queens problem.

To test your code, write a main method which takes 'N' from the user and creates a random initial N by N board, where each row (or column) of the board contains exactly one queen. However, this initial random board may not be a solution (all non-attacking placements). Solve the problem by local search calling appropriate method and print the best solution (the N by N board) found by the local search algorithm (Note that the
algorithm may not always give you the solution with all non-attacking positions). 

* Print the number of moves taken by the local search algorithm and also the successive objection function values as the algorithm progresses from the initial random board to the final solution board.

### Solution

* Objective Function taken: Maximize (negative(number_of_pairs_of_queens_that_attack_each_other)
* Expected Objective Function Value for Global Optima = 0
* Neighbour generation: For a particular column, move the queen to any row in the column other than the one it's currently in

### Execution

1. Run the file nQueens.py
2. Enter the value of 'N' when prompted to do so. Here, 'N' is the number of rows or the number of columns of the chessboard.
3. The solution should appear on the console in the following format:

* Case 1: The program successfully finds the global optima 

Enter the value of N: 8
Initial Board:
. . . . . . . .
. . . . Q . . .
. . . . . Q . .
. Q . . . . . .
Q . . . . . Q .
. . . Q . . . Q
. . Q . . . . .
. . . . . . . .

0) Current Objective Function Value:  -28
1) Current Objective Function Value:  -22
2) Current Objective Function Value:  -16
3) Current Objective Function Value:  -11
4) Current Objective Function Value:  -7
5) Current Objective Function Value:  -3
6) Current Objective Function Value:  -2
7) Current Objective Function Value:  -1
8) Current Objective Function Value:  0

Solution found:
. . Q . . . . .
. . . . . Q . .
. . . . . . . Q
. Q . . . . . .
. . . Q . . . .
Q . . . . . . .
. . . . . . Q .
. . . . Q . . .


Number of moves: 8

----------------------------------------------

* Case 2: The program cannot find the global optima and can't improve over a local optima

Enter the value of N: 8
Initial Board:
. . . . . . . .
. . . . Q Q . .
. . . . . . . .
. . . . . . . .
. . . . . . . Q
. Q . . . . Q .
. . Q Q . . . .
Q . . . . . . .

0) Current Objective Function Value:  -28
1) Current Objective Function Value:  -22
2) Current Objective Function Value:  -16
3) Current Objective Function Value:  -11
4) Current Objective Function Value:  -6
5) Current Objective Function Value:  -4
6) Current Objective Function Value:  -3
7) Current Objective Function Value:  -2
8) Current Objective Function Value:  -1

Local maxima found:
. . . . . . . Q
. . . Q . . . .
. Q . . . . . .
. . . . . . . .
. . Q . . Q . .
Q . . . . . . .
. . . . . . Q .
. . . . Q . . .


Value of objective function: -1

Number of moves: 8

----------------------------------------------