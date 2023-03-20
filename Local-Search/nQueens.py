# Given to you as attachments are two files - search.py and utils.py. 
# In search.py, there is an implementation of an abstract class 'Problem' 
# and an implementation of the class 'Node'. These classes provide generic 
# interfaces to represent an AI search problem and a node in the search-space 
# respectively. Additionally, the file also provides an implementation of the 
# hill-climbing algorithm. The utils.py file implements a number of utility methods, 
# some of which are used in search.py.

# Your task in this assignment is to solve the N-Queens problem by reducing it to an 
#optimization problem and solving the same using local search algorithm. In particular,
# you have the following tasks:

# 1. Implement a sub-class of 'Problem' (say nQueens), with concrete implementation(s) of the methods required.
# 2. Modify the necessary methods in the Node class. Try minimal modification.
# 3. Modify/Use the hill-climbing algorithm to solve the N-queens problem.

# To test your code, write a main method which takes 'N' from the user and 
# creates a random initial N by N board, where each row (or column) of the 
# board contains exactly one queen. However, this initial random board may 
# not be a solution (all non-attacking placements). 

# Solve the problem by local search calling appropriate method and print  
# the best solution (the N by N board) found by the local search algorithm 
# (Note that the algorithm may not always give you the solution with all 
# non-attacking positions). Print the number of moves taken by the local 
# search algorithm and also the successive objection function values as
# the algorithm progresses from the initial random board to the final solution board.

from search import *
from utils import *
import random

# Define class for n-Queens problem
class nQueens(Problem): 
    # Initialize the board with dimensions N x N
    def __init__(self, N):
        super().__init__(tuple(range(N))) 
        # The superclass initialization takes the initial state as input,
        # which is always a tuple of integers from 0 to N-1
        self.N = N

    # Define possible actions based on current state of the board
    def actions(self, state):
        # print(state) # Print the current state for debugging purposes
        actions = [] # Initialize an empty list of actions
        for col in range(self.N): # Loop through each column
            for row in range(self.N): # Loop through each row
                # If the queen in this column is not already in this row, 
                # add an action to move it to this row
                if row != state[col]:
                    actions.append((col, row))
        return actions

    # Define the result of taking a given action
    def result(self, state, action):
        col, row = action # Unpack the action - it is a tuple of the form (column, row)
        new_state = list(state) # Convert the current state to a list so we can modify it
        new_state[col] = row # Move the queen in the specified column to the specified row
        return tuple(new_state) # Convert the modified state back to a tuple for consistency with the superclass initialization

    # Define the objective function for the problem
    def value(self, state):
        conflicts = 0 # Initialize a counter variable for the number of conflicts between queens
        for col1 in range(self.N - 1): # Loop through each pair of columns, skipping the last one (no pairs beyond that to compare to)
            for col2 in range(col1 + 1, self.N): # Loop through each pair of columns after the current one (don't repeat comparisons between pairs)
                # Get the rows of the two queens in the current pair of columns
                row1, row2 = state[col1], state[col2]
                # If the two queens are horizontally or diagonally adjacent, there is a conflict - add 1 to the counter
                if row1 == row2 or abs(row1 - row2) == (col2 - col1):
                    conflicts += 1
        # We want to minimize this value, so the less conflicts the better
        # Therefore, we return the negative number of conflicts as the value of this state
        return -conflicts # Return the negative number of conflicts as the value of this state

# Generate a random board of size N x N
def random_board(N): # Note: Initially, there is only one queen in each column
    board = [] # Initialize an empty list to store the board
    for col in range(N): # Loop through each column
        row = random.randint(0, N - 1) # Generate a random row number for the queen in this column
        board.append(row) # Add the row number to the board
    return tuple(board) # Convert the board to a tuple for consistency with the superclass initialization

# Print the board in a readable format
def print_board(board): 
    for row in range(len(board)): # Loop through each row
        line = "" # Initialize an empty string to store the current line
        for col in range(len(board)): # Loop through each column
            if board[col] == row: # If the queen in this column is in this row
                line += "Q " # Add a Q to the line
            else: # Otherwise
                line += ". " # Add a . to the line
        print(line) # Print the line
    print() # Print a blank line to separate the boards

# Main method
if __name__ == '__main__': 
    N = int(input("Enter the value of N: ")) # Get the value of N from the user
    problem = nQueens(N) # Initialize the problem
    initial_board = random_board(N) # Generate a random initial board
    print("Initial Board:") 
    print_board(initial_board) # Print the initial board
    initial_node = Node(initial_board) # Initialize the initial node
    solution_node = hill_climbing(problem) # Solve the problem using hill-climbing
    if problem.value(solution_node.state) == 0: # If the value of the solution node is 0, we have found a solution
        print("\nSolution found:")
        print_board(solution_node.state) # Print the solution board
        print("\nNumber of moves:", solution_node.path_cost) # Print the number of moves taken to reach the solution
    else: # Otherwise, we have found a local maximum
        print("\nLocal maxima found:")
        print_board(solution_node.state) # Print the local maximum board
        print("\nValue of objective function:", problem.value(solution_node.state)) # Print the value of the objective function at the local maximum
        print("\nNumber of moves:", solution_node.path_cost) # Print the number of moves taken to reach the solution
