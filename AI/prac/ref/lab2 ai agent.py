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
