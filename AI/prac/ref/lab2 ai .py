import random

class GridEnvironment:
    def __init__(self, N, entry_point, gold_location, charging_station):
        self.N = N
        self.grid = [[None for _ in range(N)] for _ in range(N)]
        self.entry_point = entry_point
        self.gold_location = gold_location
        self.charging_station = charging_station
        self.agent_position = entry_point
        self.visited_rooms = set()

    def is_wall(self, x, y):
        return x < 0 or y < 0 or x >= self.N or y >= self.N

    def is_gold_room(self, x, y):
        return (x, y) == self.gold_location

    def is_charging_station(self, x, y):
        return (x, y) == self.charging_station

    def mark_visited(self, x, y):
        self.visited_rooms.add((x, y))

    def is_visited(self, x, y):
        return (x, y) in self.visited_rooms



class Agent:
    def __init__(self, env, X):
        self.env = env
        self.battery = X
        self.max_battery = X
        self.position = env.entry_point
        self.steps_taken = 0
        self.path_to_entry = []
        self.has_gold = False

    def move(self, dx, dy):
        new_x, new_y = self.position[0] + dx, self.position[1] + dy
        if not self.env.is_wall(new_x, new_y):
            self.position = (new_x, new_y)
            self.steps_taken += 1
            self.env.mark_visited(new_x, new_y)
            self.battery -= 1
            self.path_to_entry.append(self.position)

            if self.env.is_gold_room(new_x, new_y):
                print(f"Pot of gold found at {self.position}")
                self.has_gold = True

            if self.battery == 0:
                self.return_to_charging_station()
        else:
            print(f"Hit a wall at ({new_x}, {new_y}), changing direction.")

    def return_to_charging_station(self):
        print(f"Returning to charging station from {self.position} with {self.battery} battery left.")
        # Simulate return (we can improve this by using pathfinding algorithms)
        self.position = self.env.charging_station
        self.battery = self.max_battery
        self.steps_taken += len(self.path_to_entry)
        self.path_to_entry = []

    def explore(self):
        while not self.has_gold:
            # Simple exploration strategy: move east, then south if blocked, and so on
            if not self.env.is_wall(self.position[0] + 1, self.position[1]):  # Try moving east
                self.move(1, 0)
            elif not self.env.is_wall(self.position[0], self.position[1] + 1):  # Try moving south
                self.move(0, 1)
            elif not self.env.is_wall(self.position[0] - 1, self.position[1]):  # Try moving west
                self.move(-1, 0)
            elif not self.env.is_wall(self.position[0], self.position[1] - 1):  # Try moving north
                self.move(0, -1)

            if self.has_gold:
                print(f"Returning with the pot of gold from {self.position}")
                self.return_to_charging_station()
                break

if __name__ == "__main__":
    N = 5  # Grid size
    X = 10  # Battery capacity
    entry_point = (0, 0)
    gold_location = (3, 3)  # Gold is located at this room
    charging_station = (0, 0)

    env = GridEnvironment(N, entry_point, gold_location, charging_station)
    agent = Agent(env, X)

    agent.explore()

    print(f"Total steps taken: {agent.steps_taken}")
