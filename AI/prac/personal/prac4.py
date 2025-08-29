from collections import deque

def bfs(graph, start):
    """Perform BFS traversal from the starting node."""
    visited = set()           # Set to keep track of visited nodes
    queue = deque([start])    # Queue for BFS
    result = []               # List to store traversal order

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)         # Mark node as visited
            result.append(node)       # Add to result
            queue.extend(graph[node]) # Add unvisited neighbors to the queue

    return result

# Example graph as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Perform BFS starting from 'A'
bfs_result = bfs(graph, 'A')
print("BFS Traversal:", bfs_result)
