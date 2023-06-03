# SAT Plan Encoding for Robot Navigation Problem

* The robot can move to one of its its neighbour cells (up, down, left, right) in each step.
* There are obstacles in some of the cells of the maze, where the robot cannot enter. 
* These obstacles are present in the cells [2,2], [3,3] , [3,4] and [4,1] 

(the first number reads the column and the second reads the row. [1,1] is the bottom left corner of the maze)

The path plan should consider the basic assumptions like the robot cannot be in more than one cell at a time, it cannot pass via obstacles and it must move to reach the destination and must move in single steps.

Run the code here: https://compsys-tools.ens-lyon.fr/z3/index.php

Note: Couldn't solve the problem. Tried to encode the problem, but couldn't implement time steps. 
