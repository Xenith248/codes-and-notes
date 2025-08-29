import heapq

class KnapsackAStar:
    def __init__(self, weights, values, capacity):
        self.weights = weights  # List of weights
        self.values = values    # List of values
        self.capacity = capacity
        self.n = len(weights)   # Number of items

    def heuristic(self, idx, current_weight, current_value):
        """Calculate the heuristic value."""
        remaining_capacity = self.capacity - current_weight
        remaining_value = 0
        for i in range(idx, self.n):
            if self.weights[i] <= remaining_capacity:
                remaining_value += self.values[i]
                remaining_capacity -= self.weights[i]
        return current_value + remaining_value

    def a_star(self):
        """Solve the knapsack problem using A*."""
        # Priority queue: (priority, current_value, current_weight, index, items_included)
        pq = []
        heapq.heappush(pq, (-0, 0, 0, 0, []))  # Start with index 0

        best_value = 0
        best_items = []

        while pq:
            _, current_value, current_weight, idx, items_included = heapq.heappop(pq)

            # Check if we've reached the end of the items
            if idx == self.n:
                if current_value > best_value:
                    best_value = current_value
                    best_items = items_included
                continue

            # Exclude current item
            heapq.heappush(pq, (-self.heuristic(idx + 1, current_weight, current_value), 
                                current_value, current_weight, idx + 1, items_included))

            # Include current item (if it fits)
            if current_weight + self.weights[idx] <= self.capacity:
                heapq.heappush(pq, (-self.heuristic(idx + 1, 
                                                     current_weight + self.weights[idx], 
                                                     current_value + self.values[idx]), 
                                    current_value + self.values[idx], 
                                    current_weight + self.weights[idx], 
                                    idx + 1, 
                                    items_included + [idx]))

        return best_value, best_items

# Example
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5

solver = KnapsackAStar(weights, values, capacity)
best_value, best_items = solver.a_star()

print("Maximum Value:", best_value)
print("Items Included:", best_items)
