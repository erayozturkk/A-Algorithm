#import the maze.py file
from maze import *
from functions import *

maze = Maze(6) #initialize a 6x6 maze
maze.customize_maze() #customize the maze
maze.print_maze() #print the maze


FRONTIER = []

FRONTIER.append(maze.agent_node)
print("F value of agent ", maze.agent_node.f_value())


while goal_test(maze) == False:
    #pop the first element from the frontier
    current_state = FRONTIER.pop(0)
    print("Current state: ",current_state.position)

    #successor_state_function
    for state in successor_state_function(current_state,maze):
        FRONTIER.append(state)
    
    # get the first element from the frontier
    n = FRONTIER.pop(0)
    n.parent = current_state


    

