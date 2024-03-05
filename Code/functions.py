def successor_state_function(parentstate, maze):
    # Returns a list of all the possible successor states from the current state
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # up, down, left, right
    successors = []

    for dx, dy in directions:
        state = parentstate
        movecount = 0
        colorcount = 0

        while state and state.cell_type != 'X':
            state = maze.get_cell(state.position[0] + dx, state.position[1] + dy)
            if state:
                movecount += 1
                if state.cell_type == '0':
                    colorcount += 1
                next_state = maze.get_cell(state.position[0] + dx, state.position[1] + dy)
                if next_state == None or next_state.cell_type == 'X':
                    state.h = parentstate.h - colorcount
                    state.g = parentstate.g + movecount
                    successors.append(state)

    successors.sort(key=lambda x: x.f_value())
    return successors


def goal_test(maze):
    # returns True if all of the cells are visited
    for row in maze.maze:
        for cell in row:
            if cell.cell_type == '0':
                return False