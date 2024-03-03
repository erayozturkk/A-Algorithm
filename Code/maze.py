# Description: This file contains the node class which is used to represent a cell in the grid.
class node:
    def __init__(self, position, cell_type = '0'):
        self.position = position
        self.cell_type = cell_type
        self.h = float('inf')
        self.g = float('inf')
        self.up = None
        self.down = None
        self.left = None
        self.right = None
        
class Maze:
    def __init__(self, size):
        self.maze = self.initialize_maze(size)
        self.agent_location = None
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
                    self.agent_location = self.maze[row][col]

    def print_maze(self):
        # Print the maze
        for row in self.maze:
            for cell in row:
                print(cell.cell_type, end = ' ')
            print()