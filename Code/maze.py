# Description: This file contains the node class which is used to represent a cell in the grid.
class node:
    def __init__(self, position, cell_type = '0'):
        self.position = position
        self.cell_type = cell_type
        self.up = None
        self.down = None
        self.left = None
        self.right = None
    

class Maze:
    def __init__(self, size):
        self.maze = self.initialize_maze(size)
        self.agent_node= None
    def initialize_maze(self,size):
        # Initializes a 6x6 maze with all cells as empty ('0') by default
        maze = [[node((row, col), '0') for col in range(size)] for row in range(size)]
        #set the pointers for each cell
        for row in range(size):
            for col in range(size):
                if row > 0:
                    maze[row][col].up = maze[row-1][col]
                if row < size-1:
                    maze[row][col].down = maze[row+1][col]
                if col > 0:
                    maze[row][col].left = maze[row][col-1]
                if col < size-1:
                    maze[row][col].right = maze[row][col+1]
        return maze

    def customize_maze(self):
        # Let the user input the state of each cell
        maze_config = input("Enter all of the maze configuration as a sequence of characters without any space between them (0, X, S) : ")

        for row in range(len(self.maze)):
            for col in range(len(self.maze[0])):
                self.maze[row][col].cell_type = maze_config[row*len(self.maze[0]) + col].upper()
                if maze_config[row*len(self.maze[0]) + col].upper() == 'S':
                    self.agent_node = self.maze[row][col]
                    
    def admissible_heuristic(self):
        # Returns the admissible heuristic value for the given cell
        return sum(cell.cell_type == '0' for row in self.maze for cell in row)

    def print_maze(self):
        # Print the maze
        for row in self.maze:
            for cell in row:
                print(cell.cell_type, end = ' ')
            print()
        print('\n')

    def get_cell(self, row, col):
        # Returns the cell at the given position
        if row < 0 or row >= len(self.maze) or col < 0 or col >= len(self.maze[0]):
            return None
        return self.maze[row][col]
    
    def deepcopy_maze(self):
        # Returns a deep copy of the maze
        new_maze = Maze(len(self.maze))
        for row in range(len(self.maze)):
            for col in range(len(self.maze[0])):
                new_maze.maze[row][col].cell_type = self.maze[row][col].cell_type
        new_maze.agent_node = new_maze.get_cell(self.agent_node.position[0], self.agent_node.position[1])
        return new_maze
    
class state:
    def __init__(self,maze):
        self.maze = maze
        self.agent_position = maze.agent_node.position
        self.h_value = 0
        self.g_value = 0
        self.parent = None
    
    def successor_states(self):
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # Up, Down, Left, Right
        successors = []

        for dx, dy in directions:
            new_maze = self.maze.deepcopy_maze()
            movecount = 0
            colorcount = 0
            
            current_cell = new_maze.get_cell(self.agent_position[0], self.agent_position[1])
            next_cell = new_maze.get_cell(self.agent_position[0] + dx, self.agent_position[1] + dy)
            while next_cell and next_cell.cell_type != 'X':
                current_cell.cell_type = 'V'
                movecount += 1
                if next_cell.cell_type == '0':
                    colorcount += 1
                current_cell = next_cell
                next_cell = new_maze.get_cell(next_cell.position[0] + dx, next_cell.position[1] + dy)
                if next_cell == None or next_cell.cell_type == 'X':
                    current_cell.cell_type = 'V'
                    new_maze.agent_node = current_cell
                    successor_state = state(new_maze)
                    successor_state.parent = self
                    successor_state.g_value = self.g_value + movecount
                    successor_state.h_value = successor_state.maze.admissible_heuristic()
                    successors.append(successor_state)
                    


        return successors
    
    
    def f_value(self):# f(n) = g(n) + h(n) where g(n) is the cost to reach the node and h(n) is the heuristic value
        return self.g_value + self.h_value
    
