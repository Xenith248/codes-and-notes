from collections import deque


def bfs(graph, start_node, goal_node):

    queue = deque([[start_node]])
    visited = set()
    
    while queue:
        
        path = queue.popleft()
        node = path[-1]
        
        
        print(f"Queue: {list(queue)}")
        print(f"Total nodes in queue: {sum(len(p) for p in queue)}")
        
        
        if node == goal_node:
            print(f"Optimal path: {path}")
            return path
        
        for neighbor, connected in enumerate(graph[node]):
            if connected and neighbor not in path:
                new_path = list(path)  
                new_path.append(neighbor)  
                queue.append(new_path)  


graph = [
    [0, 1, 1, 0, 0], 
    [1, 0, 1, 1, 0],  
    [1, 1, 0, 0, 1],  
    [0, 1, 0, 0, 1],  
    [0, 0, 1, 1, 0],  
]


start_node = int(input("Enter the start node: "))
goal_node = int(input("Enter the goal node: "))

1
bfs(graph, start_node, goal_node)
