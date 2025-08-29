def fractional_knapsack(weights, profits, remaining_capacity, start_index):
    total_profit = 0
    
    for i in range(start_index, len(weights)):
        if weights[i] <= remaining_capacity:

            remaining_capacity -= weights[i]
            total_profit += profits[i]
        else:

            total_profit += (profits[i] / weights[i]) * remaining_capacity
            break

    return total_profit

def a_star_knapsack(index, N, W, weights, profits, solution, current_weight, current_profit, current_best_profit, current_best_solution):

    if index == N:
        print(f"Solution: {solution}, Weight: {current_weight}, Profit: {current_profit}")

        if current_weight <= W and current_profit > current_best_profit[0]: 
            current_best_profit[0] = current_profit
            current_best_solution[:] = solution[:] 
        
        return

    if current_weight > W:
        print(f"Pruning: {solution}, Weight exceeds capacity")
        return

    max_estimated_profit = current_profit + fractional_knapsack(weights, profits, W - current_weight, index)

    if max_estimated_profit < current_best_profit[0]:
        print(f"Pruning: {solution}, Max estimated profit is less than current best profit")
        return

    solution[index] = 1
    a_star_knapsack(index + 1, N, W, weights, profits, solution, current_weight + weights[index], current_profit + profits[index], current_best_profit, current_best_solution)

    solution[index] = 0
    a_star_knapsack(index + 1, N, W, weights, profits, solution, current_weight, current_profit, current_best_profit, current_best_solution)

def knapsack_a_star(N, W, weights, profits):
    
    ratio = [profits[i] / weights[i] for i in range(N)]
    sorted_indices = sorted(range(N), key=lambda i: ratio[i], reverse=True)
    weights = [weights[i] for i in sorted_indices]
    profits = [profits[i] for i in sorted_indices]

    solution = [-1] * N  
    current_best_solution = [-1] * N  
    current_best_profit = [-float('inf')]  

    a_star_knapsack(0, N, W, weights, profits, solution, 0, 0, current_best_profit, current_best_solution)

    print(f"\nBest Profit: {current_best_profit[0]}")
    print(f"Best Solution: {current_best_solution}")

N = 4
W = 10
weights = [2, 3, 4, 5] 
profits = [3, 4, 5, 6]  

knapsack_a_star(N, W, weights, profits)