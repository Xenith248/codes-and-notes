from collections import deque


initial_state = ('L', 'L', 'L', 'L') 
goal_state = ('R', 'R', 'R', 'R')  

def get_possible_moves(state):
    """Generate all legal next states from the current state."""
    farmer, wolf, goat, cabbage = state
    new_states = []

    # Farmer moves alone
    if farmer == 'L':
        new_states.append(('R', wolf, goat, cabbage))  # Farmer takes no one
    else:
        new_states.append(('L', wolf, goat, cabbage))  # Farmer returns alone

    # Farmer moves with the wolf
    if farmer == wolf:
        if farmer == 'L':
            new_states.append(('R', 'R', goat, cabbage))  # Take wolf
        else:
            new_states.append(('L', 'L', goat, cabbage))  # Return with wolf

    # Farmer moves with the goat
    if farmer == goat:
        if farmer == 'L':
            new_states.append(('R', wolf, 'R', cabbage))  # Take goat
        else:
            new_states.append(('L', wolf, 'L', cabbage))  # Return with goat

    # Farmer moves with the cabbage
    if farmer == cabbage:
        if farmer == 'L':
            new_states.append(('R', wolf, goat, 'R'))  # Take cabbage
        else:
            new_states.append(('L', wolf, goat, 'L'))  # Return with cabbage

    return new_states

def is_valid_state(state):
    """Check if the state is valid."""
    farmer, wolf, goat, cabbage = state
    # If the farmer is not present and the wolf is with the goat or the goat is with the cabbage
    if farmer != goat and wolf == goat:
        return False  # Invalid: wolf eats goat
    if farmer != goat and goat == cabbage:
        return False  # Invalid: goat eats cabbage
    return True  # Valid state

def bfs_solve_puzzle():
    """Solve the puzzle using BFS."""
    queue = deque([initial_state])
    visited_states = set([initial_state])

    while queue:
        current_state = queue.popleft()
        print(f"Current State: {current_state}")

        # If the goal state is reached
        if current_state == goal_state:
            print("Goal reached!")
            return

        # Get all possible moves from the current state
        for next_state in get_possible_moves(current_state):
            if next_state not in visited_states and is_valid_state(next_state):
                visited_states.add(next_state)
                queue.append(next_state)

# Run the BFS solver
bfs_solve_puzzle()
