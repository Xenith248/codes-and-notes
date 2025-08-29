from queue import PriorityQueue

class KnapsackSolver:
    def __init__(self, profits, weights, capacity):
        self.profits = profits
        self.weights = weights
        self.capacity = capacity
        self.n = len(profits)
        self.best_profit = float('-inf')
        self.best_solution = [-1] * self.n
        self.best_weight = 0  # To keep track of the best weight

    def fractional_knapsack(self, remaining_capacity, idx):
        """Fractional knapsack heuristic to estimate the maximum profit from remaining items."""
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
        pq = PriorityQueue() 
        # -1 indicating no decision has been made
        initial_node = (0, 0, 0, [-1] * self.n)  # (negative profit estimate, current profit, current weight, solution vector)
        pq.put(initial_node)
        
        while not pq.empty():
            neg_estimated_profit, current_profit, current_weight, solution = pq.get()
            
            d = solution.count(-1)  # Count undecided elements (depth of search)
            if d == 0:  # Leaf node
                if current_profit > self.best_profit:
                    self.best_profit = current_profit
                    self.best_weight = current_weight  # Track the total weight of the best solution
                    self.best_solution = solution[:]
            else:
                idx = self.n - d
                # Option 1: Include item at index idx if it doesn't exceed the capacity
                if current_weight + self.weights[idx] <= self.capacity:
                    new_solution = solution[:]
                    new_solution[idx] = 1
                    self._explore_node(new_solution, current_profit + self.profits[idx], current_weight + self.weights[idx], idx, pq)

                # Option 2: Do not include item at index idx
                new_solution = solution[:]
                new_solution[idx] = 0
                self._explore_node(new_solution, current_profit, current_weight, idx, pq)

        return self.best_profit, self.best_weight, self.best_solution

    def _explore_node(self, solution, current_profit, current_weight, idx, pq):
        remaining_capacity = self.capacity - current_weight
        estimated_profit = current_profit + self.fractional_knapsack(remaining_capacity, idx + 1)
        
        if estimated_profit > self.best_profit:  # Only explore if the estimate is promising
            pq.put((-estimated_profit, current_profit, current_weight, solution))


profits = [80, 100, 120]
weights = [30, 50, 10]
capacity = 60

solver = KnapsackSolver(profits, weights, capacity)
best_profit, best_weight, best_solution = solver.a_star()


print(f"Best Profit: {best_profit}")
print(f"Best Weight: {best_weight}")
print(f"Best Solution: {best_solution}")
