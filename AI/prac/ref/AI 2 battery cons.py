class Environment:
    def __init__(self, N, entry_point, gold_location, charging_station):
        self.N = N  # Grid size N x N
        self.entry_point = entry_point  # Entry point location
        self.gold_location = gold_location  # Gold location (unknown to agent initially)
        self.charging_station = charging_station  # Charging station location
        self.grid = [[False for _ in range(N)] for _ in range(N)]  # Explored grid
        self.agent_position = entry_point
        self.visited = set()  # Keep track of visited rooms

    def is_within_bounds(self, x, y):
        return 0 <= x < self.N and 0 <= y < self.N

    def mark_visited(self, x, y):
        self.visited.add((x, y))
        self.grid[x][y] = True

    def is_gold_found(self, x, y):
        return (x, y) == self.gold_location

    def is_charging_station(self, x, y):
        return (x, y) == self.charging_station

class Agent:
    def __init__(self, env, battery_capacity):
        self.env = env
        self.battery = battery_capacity  # Full battery capacity
        self.max_battery = battery_capacity  # Store max battery capacity
        self.steps_taken = 0  # Total steps taken
        self.position = env.entry_point  # Current position of the agent
        self.path_memory = []  # To store the path for backtracking
        self.has_gold = False  # Gold status
        self.visited = set()  # Rooms the agent has already visited
        self.direction_memory = {}  # Directions tried for each room

    def distance_to_charging_station(self):
        """Calculate the distance (in steps) back to the charging station (entry point)."""
        return len(self.path_memory)  # Distance is the length of the path back

    def can_return_to_charging_station(self):
        """Check if the agent has enough battery to return to the charging station."""
        return self.battery >= self.distance_to_charging_station()

    def move(self, dx, dy):
        new_x, new_y = self.position[0] + dx, self.position[1] + dy
        if self.env.is_within_bounds(new_x, new_y) and (new_x, new_y) not in self.visited:
            # Move to the new position
            self.position = (new_x, new_y)
            self.steps_taken += 1
            self.env.mark_visited(new_x, new_y)
            self.battery -= 1
            self.path_memory.append(self.position)
            self.visited.add(self.position)

            if self.env.is_gold_found(new_x, new_y):
                self.has_gold = True
                print(f"Gold found at {self.position}!")
            if not self.can_return_to_charging_station():
                self.return_to_charging()
            return True  # Successful move
        else:
            return False  # Failed move (hit wall or revisited room)

    def return_to_charging(self):
        """Return to the charging station, consuming battery as the agent backtracks."""
        print(f"Returning to charging station from {self.position}")

        while self.position != self.env.charging_station:
            if self.battery == 0:
                print("Battery depleted before reaching the charging station!")
                break
            self.position = self.path_memory.pop()  # Backtrack along the path
            self.battery -= 1
            self.steps_taken += 1

        if self.position == self.env.charging_station:
            print(f"Reached the charging station at {self.position}.")
            self.battery = self.max_battery
            self.path_memory = []  # Clear path memory after recharging

    def explore(self):
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # East, South, West, North
        while not self.has_gold:
            # Get the untried directions for the current room
            if self.position not in self.direction_memory:
                self.direction_memory[self.position] = set()

            untried_directions = [i for i in range(4) if i not in self.direction_memory[self.position]]

            if not untried_directions:
                # If no untried directions, backtrack
                if self.path_memory:
                    print(f"Backtracking from {self.position}")
                    self.position = self.path_memory.pop()
                continue

            direction_index = untried_directions[0]  # Try the first untried direction
            self.direction_memory[self.position].add(direction_index)  # Mark this direction as tried
            dx, dy = directions[direction_index]

            if self.move(dx, dy):  # If the move is successful
                if self.has_gold:
                    print(f"Returning to entry point from {self.position}")
                    self.return_to_charging()  # Return to charging station or entry point
                    break
            else:
                print(f"Hit a wall or visited room at ({self.position[0] + dx}, {self.position[1] + dy}), trying a different direction.")





if __name__ == "__main__":
    N = 5  # Grid size
    X = 10  # Battery capacity
    entry_point = (0, 0)
    gold_location = (1, 3)
    charging_station = (0, 0)

    env = Environment(N, entry_point, gold_location, charging_station)
    agent = Agent(env, X)

    agent.explore()

    print(f"Total steps taken: {agent.steps_taken}")
