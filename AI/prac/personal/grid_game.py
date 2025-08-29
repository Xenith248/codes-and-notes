import random

class GridGame:
    def __init__(self, n):
        """Initialize the grid and game variables."""
        self.n = n
        self.grid = [[0 for _ in range(n)] for _ in range(n)]
        self.player_position = (0, 0)
        self.goal_position = (n - 1, n - 1)
        self.generate_obstacles()

    def generate_obstacles(self):
        """Randomly generate obstacles on the grid."""
        num_obstacles = random.randint(self.n, self.n * 2)  # Random number of obstacles
        for _ in range(num_obstacles):
            x, y = random.randint(0, self.n - 1), random.randint(0, self.n - 1)
            if (x, y) not in [self.player_position, self.goal_position]:
                self.grid[x][y] = 1  # Mark as obstacle

    def display_grid(self):
        """Display the grid with the player's position."""
        for i in range(self.n):
            for j in range(self.n):
                if (i, j) == self.player_position:
                    print("P", end=" ")  # Player
                elif (i, j) == self.goal_position:
                    print("G", end=" ")  # Goal
                elif self.grid[i][j] == 1:
                    print("X", end=" ")  # Obstacle
                else:
                    print(".", end=" ")  # Empty cell
            print()
        print("-" * (self.n * 2))

    def move_player(self, direction):
        """Move the player in the specified direction."""
        x, y = self.player_position
        if direction == "up" and x > 0:
            new_position = (x - 1, y)
        elif direction == "down" and x < self.n - 1:
            new_position = (x + 1, y)
        elif direction == "left" and y > 0:
            new_position = (x, y - 1)
        elif direction == "right" and y < self.n - 1:
            new_position = (x, y + 1)
        else:
            print("Invalid move!")
            return

        # Check if the new position is valid
        if self.grid[new_position[0]][new_position[1]] == 1:
            print("Hit an obstacle! Try a different direction.")
        else:
            self.player_position = new_position

    def play(self):
        """Run the game loop."""
        print("Welcome to the Grid Game!")
        print("Navigate from P (Player) to G (Goal) avoiding obstacles (X).")
        print("Enter 'up', 'down', 'left', or 'right' to move.")
        while self.player_position != self.goal_position:
            self.display_grid()
            move = input("Your move: ").strip().lower()
            self.move_player(move)
        print("Congratulations! You reached the goal!")
        self.display_grid()

# Run the game
grid_size = 10  # Set the size of the grid (n x n)
game = GridGame(grid_size)
game.play()
