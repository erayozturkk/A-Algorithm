#import the maze.py file
from maze import *
from functions import *


maze = Maze(6) #initialize a 6x6 maze
maze.customize_maze() #customize the maze
maze.print_maze() #print the maze

current_state = state(maze) #initialize the current state

FRONTIER = PriorityQueue()
FRONTIER.append(current_state)
CLOSED = []
print("F value of state 0:", current_state.f_value())


while goal_test(current_state.maze) == False:
    #pop the first element from the frontier
    current_state = FRONTIER.pop(0)
    print("Current state: ", '\n')
    current_state.maze.print_maze()

    #successor_state_function
    for state in current_state.successor_states():
        if state in CLOSED:
            continue
        elif state in FRONTIER.queue:
            index = FRONTIER.queue.index(state)
            if state.f_value < FRONTIER.queue[index].f_value:
                FRONTIER.pop(index)
                FRONTIER.append(state)
        else:
            FRONTIER.append(state)
            print("Successor state: ", '\n')
            state.maze.print_maze()
    CLOSED.append(current_state)

print("SOLUTION: ", '\n')
while current_state.parent != None:
    
    print("Current state: ", '\n')
    current_state.maze.print_maze()
    current_state = current_state.parent
    




    

