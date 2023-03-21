# Knowledge Based Agent

## Implement a knowledge-based agent to solve the Wumpus World problem. 

The problem is simplified in the assignment in the following ways:
1. There is no arrow with the agent.
2. Since there is no arrow, the agent is always living. There is no 'scream' sensing.
3. The agent wins the game by finding the gold. That is, there is no need to come out of the cave.

As part of the assignment, you are provided with Python library implementation of the logical inference routines such as tt_entailment and pl_resolution as discussed in the class and also relevant library methods like to_cnf() etc. Routines to create the knowledge-base is also provided along with a number of other utility methods. These implementations are by the author of the AIMA book, Peter Norvig. Your task in the assignment is the following:

1. Complete the implementation of the function choose_location(self, x , y, cave_size) in the inference.py file. The parameters are the current agent location and the cave size and it must return the next safe location, if any. The choice made should be logical based on inference methods.

2. Complete the implementation of the safe() and not_safe() methods of the WumpusWorldAgent class. The safe() method must return the set of safe locations to move to. The not_safe() method must return the set of locations that can't be proven unsafe to move to.

The main() method in _wumpusworld.py_ calls two game instances. Your implementation should be such that the agent wins both the games.

#### Execution Instructions

> Run the wumpusworld.py file.