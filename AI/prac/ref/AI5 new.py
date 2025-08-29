from queue import PriorityQueue

class KnapsackSolver:
    def __init__(self, profits, weights, capacity):
        self.profits = profits
        self.weights = weights
        self.capacity = capacity
        self.n = len(profits)
        self.best_profit = float('-inf')
        self.best_solution = [-1] * self.n

    def fractional_knapsack(self, remaining_capacity, idx):
        """
        Fractional knapsack heuristic to estimate the maximum profit from remaining items.
        This function estimates the maximum profit that can be obtained with fractional items.
        """
        total_value = 0
        for i in range(idx, self.n):
            if self.weights[i] <= remaining_capacity:
                remaining_capacity -= self.weights[i]
                total_value += self.profits[i]
            else:
                total_value += self.profits[i] * (remaining_capacity / self.weights[i])
                break
        return total_value

    def a_star(self):
        # Priority queue to explore nodes based on their heuristic value (maximum estimated profit)
        pq = PriorityQueue()
        # Initial node: (negative estimated profit, current profit, current weight, decision vector S)
        initial_node = (0, 0, 0, [-1] * self.n)
        pq.put(initial_node)
        
        while not pq.empty():
            # Get the node with the highest estimated profit
            neg_estimated_profit, current_profit, current_weight, solution = pq.get()

            # Depth of the tree, or number of items decided so far
            d = solution.count(-1)

            if d == 0:  # Leaf node (all items have been assigned)
                # Update the best solution if this path has a higher profit
                if current_profit > self.best_profit:
                    self.best_profit = current_profit
                    self.best_solution = solution[:]
            else:
                idx = self.n - d  # Current index in the solution vector

                # Option 1: Include the item at index 'idx'
                if current_weight + self.weights[idx] <= self.capacity:
                    new_solution = solution[:]
                    new_solution[idx] = 1
                    self._explore_node(new_solution, current_profit + self.profits[idx], current_weight + self.weights[idx], idx, pq)

                # Option 2: Do not include the item at index 'idx'
                new_solution = solution[:]
                new_solution[idx] = 0
                self._explore_node(new_solution, current_profit, current_weight, idx, pq)

        return self.best_profit, self.best_solution

    def _explore_node(self, solution, current_profit, current_weight, idx, pq):
        """
        Helper function to calculate the heuristic and explore the node.
        Adds new nodes to the priority queue if the estimated profit is promising.
        """
        remaining_capacity = self.capacity - current_weight
        # Calculate estimated profit using the fractional knapsack for remaining items
        estimated_profit = current_profit + self.fractional_knapsack(remaining_capacity, idx + 1)

        # Only explore further if the estimated profit is higher than the best profit so far
        if estimated_profit > self.best_profit:
            pq.put((-estimated_profit, current_profit, current_weight, solution))

# Example usage:
profits = [60, 100, 120]  # Profits for the items
weights = [10, 20, 30]    # Weights for the items
capacity = 50             # Knapsack capacity

# Initialize the solver
solver = KnapsackSolver(profits, weights, capacity)

# Run the A* algorithm
best_profit, best_solution = solver.a_star()

# Output the best solution
print
