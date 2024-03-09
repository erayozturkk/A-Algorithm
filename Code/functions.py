
def goal_test(maze):
    # returns True if all of the cells are visited
    for row in maze.maze:
        for cell in row:
            if cell.cell_type == '0':
                return False
            
#PriorityQueue class is used to implement the frontier. It is a list of states that are sorted based on their f value.
class PriorityQueue:
    def __init__(self):
        self.queue = []

    def append(self, state):
        self.queue.append(state)
        self.queue.sort(key=lambda x: x.f_value())

    def pop(self, index):
        return self.queue.pop(index)