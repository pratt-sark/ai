# n-puzzle problem
# As an input, you will be given an initial and a goal board configuration and your task is to find a sequence of moves that takes the initial board configuration to the goal board configuration.

# The problem formulation in terms of the state-space is as follows:

# States: Any arrangement of numbers 1-(n*n-1) on the board together with a blank cell is a state.
# Initial State: A random placement of numbers 1-(n*n-1) and the blank in the 16 cells of the board.
# Actions: up,down,left,right. The respective action swaps the number to the up,down,left,right of the blank cell with the blank cell.
# Transition Model: Returns the new board after an application of the action.
# Goal test: Whether the current state matches with the goal configuration.

# Implement the graph search algorithm to print a path from the initial state leading to the goal state along with the corresponding action sequence (initial-board – up – next-board – down – next board – ... – right – goal-board)

import numpy as np 
import random
import sys

# ----------------Global variables---------------------------------
path = [] #initialise the path
moves = [] #initialise the moves list
open = [] #list of all open nodes
closed = [] #list of all closed nodes
#------------------------------------------------------------------

# Take the value of n from the user 
# Note: User will enter 15, we will convert it to 4. 
# Similarly, user will enter 8, we will convert it to 3.
n = (int)(input("\nEnter the value of n (Eg: For 15 puzzle, enter 15): "))
n = (int)(np.sqrt(n+1)) #calculate the value of actual n (Eg: For 15 puzzle, n=4)
#------------------------------------------------------------------

def board_init(board): #initialise the board with user input
  for i in range(n): 
    print('Row ',i,':') 
    board[i] = np.array([int(x) for x in input().split()]) 
  # print("The Board is intialised as ---->\n",board)
  return board

def make_board(): #make the board
  board = np.zeros((n,n),dtype=int) #initialise the board with zeros
  board = board_init(board) #initialise the board
  return board 
#--------------------------------------------------------------------------

def move_left(board): #move the blank left
  row,col = (int)(np.where(board==0)[0]),(int)(np.where(board==0)[1]) #find the position of the blank
  if col!=0: #if the blank is not in the leftmost column
    board[row][col] = board[row][col-1] #swap the blank with the number to the left
    board[row][col-1] = 0 #make the position of the number to the left as blank
    # print("Left Move DONE.")
    return board 

def move_right(board): #move the blank right
  row,col = (int)(np.where(board==0)[0]),(int)(np.where(board==0)[1]) #find the position of the blank
  if col!=(n-1): #if the blank is not in the rightmost column
    board[row][col] = board[row][col+1] #swap the blank with the number to the right
    board[row][col+1] = 0 #make the position of the number to the right as blank
    # print("Right Move DONE.")
    return board

def move_up(board): #move the blank up
  row,col = (int)(np.where(board==0)[0]),(int)(np.where(board==0)[1])  #find the position of the blank
  if row!=0: #if the blank is not in the topmost row
    board[row][col] = board[row-1][col] #swap the blank with the number above
    board[row-1][col] = 0 #make the position of the number above as blank
    # print("Up Move DONE.")
    return board 

def move_down(board): #move the blank down
  row,col = (int)(np.where(board==0)[0]),(int)(np.where(board==0)[1]) #find the position of the blank
  if row!=(n-1): #if the blank is not in the bottommost row
    board[row][col] = board[row+1][col] #swap the blank with the number below
    board[row+1][col] = 0 #make the position of the number below as blank
    # print("Down Move DONE.")
    return board
#--------------------------------------------------------------------------

def no_of_misplaced_tiles(board,goal_board): #calculate the number of misplaced tiles
  count=0 #initialise the count to zero
  for i in range(n): #for each row
    for j in range(n): #for each column
      if board[i][j]!=goal_board[i][j]: #if the number in the board is not equal to the number in the goal board
        count+=1 #increment the count
  return count #return the count
#--------------------------------------------------------------------------

def manhattan_distance(board,goal_board): #calculate the manhattan distance
  count=0 #initialise the count to zero
  for i in range(n): #for each row
    for j in range(n): #for each column
      if board[i][j]!=goal_board[i][j]: #if the number in the board is not equal to the number in the goal board
        row,col = (int)(np.where(goal_board==board[i][j])[0]),(int)(np.where(goal_board==board[i][j])[1]) #find the position of the number in the goal board
        count += abs(row-i) + abs(col-j) #calculate the manhattan distance
  return count #return the count
#--------------------------------------------------------------------------

def h(board,goal_board): #calculate the heuristic value
  return manhattan_distance(board,goal_board) #return the manhattan distance
#--------------------------------------------------------------------------

def row_number_of_blank(board): #find the row number of the blank
  row = np.where(board==0)[0] #find the row number of the blank
  return (int)(row) #return the row number of the blank
#--------------------------------------------------------------------------

def calc_inversions(board): #calculate the number of inversions
  count=0 #initialise the count to zero
  boardlist = board.flatten().tolist() #convert the board to a list
  boardlist.remove(0) #remove the blank from the list
  # print(board_as_list)
  for i in range(len(boardlist)-1): #for each element in the list
    for j in range(i+1,len(boardlist)): #for each element in the list
      if boardlist[i]>boardlist[j]: #if the element is greater than the other element
        count+=1 #increment the count
  return count #return the count
#--------------------------------------------------------------------------

def isOdd(num): #check if the number is odd
  return num%2!=0 #return true if the number is odd
#--------------------------------------------------------------------------

def solvable(board,goal_board): #check if the board is solvable
  if isOdd(len(board)): #board length is odd
    if isOdd(calc_inversions(board)) and not(isOdd(calc_inversions(goal_board))): 
      return False
    elif isOdd(calc_inversions(goal_board)) and not(isOdd(calc_inversions(board))): 
      return False
    else:
      return True
  else: #board length is even
    sumInitBoard = calc_inversions(board)+row_number_of_blank(board) 
    sumGoalBoard = calc_inversions(goal_board)+row_number_of_blank(goal_board)
    if isOdd(sumInitBoard) and not(isOdd(sumGoalBoard)):
      return False
    elif isOdd(sumGoalBoard) and not(isOdd(sumInitBoard)):
      return False
    else:
      return True
#--------------------------------------------------------------------------

class State: #class to represent the state of the board
  left = right = up = down = parent = None #initialise the instance variables
  board = 0 #initialise the board
  prev_move = None #initialise the previous move
  h = 0 #initialise the heuristic value
  def __init__(self,board): #initialise the state
    self.board = board #set the board
  def gen_successors(self): #generate the successors
    self.left = State(move_left(self.board.copy())) #generate the left successor
    self.right = State(move_right(self.board.copy())) #generate the right successor
    self.up = State(move_up(self.board.copy())) #generate the up successor
    self.down  = State(move_down(self.board.copy())) #generate the down successor
    #set the parent of the successors
    self.left.parent = self 
    self.right.parent = self 
    self.up.parent = self
    self.down.parent = self
    #--------------------------------
    self.left.prev_move = 'Left' #set the previous move of the left successor
    self.right.prev_move = 'Right' #set the previous move of the right successor
    self.up.prev_move = 'Up' #set the previous move of the up successor
    self.down.prev_move = 'Down' #set the previous move of the down successor
    succ_list = [self.left,self.right,self.up,self.down] #create a list of successors
    succ_list = [i for i in succ_list if i.board is not None] #remove the None successors
    return succ_list #return the list of successors
#--------------------------------------------------------------------------

def goalTest(initBoard,goalBoard): #check if the board is the goal board
  for i in range(n): #for each row
    for j in range(n): #for each column
      if initBoard[i][j] != goalBoard[i][j]: #if the element is not equal to the goal element
        return False 
  return True #return true if the board is the goal board
#--------------------------------------------------------------------------

def obj_notin_list(obj,list): #check if the object is not in the list
  for i in list: #for each element in the list
    if np.array_equal(i.board,obj.board): #if the board is equal to the board of the element
      return False #return false
  return True #return true if the object is not in the list
#--------------------------------------------------------------------------

def GraphSearch(state,g):
    global open , closed, movesAndPath
    open.append(state) #initialise the open list with the initial state
    while open: #while the open list is not empty
        # print("\nIteration ",len(open))

        # s = open.pop(0) #pop the first element from the open list
        min = sys.maxsize #initialise the minimum value to -1
        s = None #initialise the state to None
        for op in open.copy():
          if h(op.board,g.board) < min:
            # print("h = ",h(op.board,g.board))
            min = h(op.board,g.board)
            s = op
        # print("Min h found = ",min)
        # print("State with min h = ",s.board)
        open.remove(s) #remove the state from the open list
        if goalTest(s.board,g.board): #if the state is the goal state
            print("\nGoal Found!")
            print("\nPath:")
            
            while s: #while the state is not None
                path.append(s) #append the state to the path
                moves.append(s.prev_move) #append the previous move to the moves list
                s = s.parent #set the state to the parent of the state
            path.reverse() #reverse the path
            moves.reverse() #reverse the moves list
            return True #return true
        else: #if the state is not the goal state
            closed.append(s) #append the state to the closed list
            succ_list = s.gen_successors() #generate the successors of the state
            # random.shuffle(succ_list)
            for i in succ_list: #for each successor
                if obj_notin_list(i,closed) and obj_notin_list(i,open): #if the successor is not in the closed list
                    open.append(i) #append the successor to the open list
    return False #return false if the goal is not found
#--------------------------------------------------------------------------

#Execution starts here

print('Enter the initial board:')
s = State(make_board())
print('\nEnter the goal board:')
g = State(make_board())

print('\n-----------SOLUTION STARTS HERE-----------')

print('\nInitial Board:')
# For n=4
# s= State(np.array([[2,3,6,4],[1,5,0,7],[10,11,12,8],[9,13,14,15]]))
# s= State(np.array([[1,2,3,4],[5,0,6,7],[8,9,10,11],[12,13,14,15]]))
print(s.board)

print('\nGoal Board:')
#Solvable instance (for n=4)
# g = State(np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]]))
#Not solvable instance (for n=4)
# g = State(np.array([[2,3,0,4],[1,5,6,7],[10,11,12,8],[9,13,14,15]]))
print(g.board)

if (solvable(s.board,g.board)): #if the board is solvable
    print("\nFor given pair of Initial and Goal State, the problem is Solvable!")
    print("\nPlease wait while the I find the solution path...")
    print("\n\nThis may take a while...\n")
    found = GraphSearch(s,g)
    if found: #if the goal is found
        moves = [m for m in moves if m is not None] # remove the None moves
        moves.append("") # add a blank move at the end to match the length of the path
        for p,m in zip(path,moves): #for each state and move
            print(p.board) #print the board
            print("\n"+str(m)) #print the move
            print("\n") #print a new line
else: #if the board is not solvable
    print("\nNot Solvable :(")