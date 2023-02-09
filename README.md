# ai
### Artificial Intelligence Lab Codes

All codes are in Jupyter Notebook format, coded in Python. Just download them and run them using Google Colab or VSCode. 
No specific inputs required except the obvious ones communicated using input prompts.

#### Uninformed Search

<details>
  <summary>### 8 Queens problem & n-Queens problem</summary>
  
  The goal of the n-queens problem is to place n queens on a chessboard such that no queen attacks any other. 
  The problem formulation in terms of the state-space is as follows:
  
  * States: Any arrangement of 0-n queens on the board is a state.
  * Initial State: No queens on the board.
  * Actions: Add a queen to any empty square.
  * Transition Model: Returns the board with a queen added to the specified square.
  * Goal test: n queens are on the board, none attacked.
  
  Write a program to:
  1. Solve the problem starting from the initial state and print the solution chessboard.
  2. Print the number of solutions to the problem.
  3. Print the number of non-attacking states.

</details>

<details>
    <summary>### 15-puzzle problem</summary>
   As an input, you will be given an initial and a
  goal board configuration and your task is to find a sequence of moves that takes the initial board
  configuration to the goal board configuration. 
    The problem formulation in terms of the state-space
  is as follows:

  1. States: Any arrangement of numbers 1-15 on the board together with a blank cell is a state.
  2. Initial State: A random placement of numbers 1-15 and the blank in the 16 cells of the board.
  3. Actions: up,down,left,right. The respective action swaps the number to the up,down,left,right
  of the blank cell with the blank cell.
  4. Transition Model: Returns the new board after an application of the action.
  5. Goal test: Whether the current state matches with the goal configuration.

  Implement the graph search algorithm to print a path from the initial state leading to the goal
  state along with the corresponding action sequence (initial-board – up – next-board – down – next
  board – ... – right – goal-board)
  </details>
