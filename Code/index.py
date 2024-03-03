#import the maze.py file
from maze import *
from functions import *

maze = Maze(6) #initialize a 6x6 maze
maze.customize_maze() #customize the maze
maze.print_maze() #print the maze

#successor_state_function
successor_states= successor_state_function(maze.agent_location, maze)
for state in successor_states:
    print("Possible next state: ",state.position)

