class Environment:
    def __init__(self, N, entry_point, gold_location, charging_station):
        self.N = N 
        self.entry_point = entry_point  
        self.gold_location = gold_location  
        self.charging_station = charging_station  
        self.grid = [[False for _ in range(N)] for _ in range(N)]  
        self.agent_position = entry_point
        self.visited = set()  

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
        self.battery = battery_capacity  
        self.max_battery = battery_capacity  
        self.steps_taken = 0  
        self.position = env.entry_point 
        self.path_memory = []  
        self.has_gold = False  
        self.visited = set()  
        self.direction_memory = {}  

    def move(self, dx, dy):
        new_x, new_y = self.position[0] + dx, self.position[1] + dy
        if self.env.is_within_bounds(new_x, new_y) and (new_x, new_y) not in self.visited:
            
            self.position = (new_x, new_y)
            self.steps_taken += 1
            self.env.mark_visited(new_x, new_y)
            self.battery -= 1
            self.path_memory.append(self.position)
            self.visited.add(self.position)

            if self.env.is_gold_found(new_x, new_y):
                self.has_gold = True
                print(f"Gold found at {self.position}!")
            if self.battery == 0:
                self.return_to_charging()
            return True  
        else:
            return False  

    def return_to_charging(self):
        print(f"Returning to charging station from {self.position}")
       
        self.position = self.env.charging_station
        self.battery = self.max_battery
        self.steps_taken += len(self.path_memory)  
        self.path_memory = []  

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
                    self.return_to_charging()
                    break
            else:
                print(f"Hit a wall or visited room at ({self.position[0] + dx}, {self.position[1] + dy}), trying a different direction.")




if __name__ == "__main__":
    N = 5  # Grid size
    X = 10  # Battery capacity
    entry_point = (0, 0)
    gold_location = (3, 3)
    charging_station = (0, 0)

    env = Environment(N, entry_point, gold_location, charging_station)
    agent = Agent(env, X)

    agent.explore()

    print(f"Total steps taken: {agent.steps_taken}")
