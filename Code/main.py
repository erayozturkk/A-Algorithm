#import the maze.py file
from maze import *
import time
import sys
row_count = int(input("Enter the number of rows: "))
col_count = int(input("Enter the number of columns: "))


maze = Maze(row_count,col_count) #initialize a  maze(row,col)
maze.customize_maze() #customize the maze
maze.print_maze() #print the maze

current_state = state(maze) #initialize the current state

FRONTIER = PriorityQueue()
FRONTIER.append(current_state)
CLOSED = []
print("F value of state 0:", current_state.f_value())

iteration = 0
#start the timer
start = time.time()
while current_state.maze.goal_test() == False and iteration < 100000:
    iteration += 1
    #pop the first element from the frontier
    current_state = FRONTIER.pop(0)
    print("Current state: ", '\n')
    current_state.maze.print_maze()

    #successor_state_function
    for state in current_state.successor_states():
        if (state.stringmaze, state.agent_position) not in  CLOSED:
            if (state.stringmaze, state.agent_position) not in [(x.stringmaze, x.agent_position)for x in FRONTIER.queue]:
                FRONTIER.append(state)
            else:
                for i in range(len(FRONTIER.queue)):
                    if FRONTIER.queue[i].stringmaze == state.stringmaze:
                        if state.f_value() < FRONTIER.queue[i].f_value():
                            FRONTIER.queue[i] = state
                            FRONTIER.queue.sort(key=lambda x: x.f_value())
        else:
            print("State already visited")
    CLOSED.append((current_state.stringmaze, current_state.agent_position))

# stop the timer
end = time.time()

if iteration == 100000:
    print("No solution found")
else:
    print("SOLUTION: ")
    total_distance = current_state.g_value
    stepcount = 0
    while current_state.parent != None:
        stepcount += 1
        print("Solution Step: ", '\n')
        current_state.maze.print_maze()
        current_state = current_state.parent
    print("Step 0: ", '\n')
    current_state.maze.print_maze()
    print("Total distance travele: ", total_distance)
    print("Total number of states in closed: ", len(CLOSED))
    print("Total number of steps: ", stepcount)
    print("Time taken: ", end - start, " seconds")
    # calculate the size of FRONTIER and CLOSED in terms of bytes
    print("Size of FRONTIER: ", sys.getsizeof(FRONTIER), " bytes")
    print("Size of CLOSED: ", sys.getsizeof(CLOSED), " bytes")


    





    

