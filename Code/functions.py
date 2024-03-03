def successor_state_function(agentstate, maze):
    # Returns a list of all the possible successor states from the current state
    state = agentstate
    successors = []
    if state.up and state.up.cell_type != 'X' :
        while state.up and state.up.cell_type != 'X':
            state = state.up
        successors.append(state)
    state = agentstate
    if state.down and state.down.cell_type != 'X':
        while state.down and state.down.cell_type != 'X':
            state = state.down
        successors.append(state)
    state = agentstate
    if state.left and state.left.cell_type != 'X':
        while state.left and state.left.cell_type != 'X':
            state = state.left
        successors.append(state)
    state = agentstate
    if state.right and state.right.cell_type != 'X':
        while state.right and state.right.cell_type != 'X':
            state = state.right
        successors.append(state)
    return successors