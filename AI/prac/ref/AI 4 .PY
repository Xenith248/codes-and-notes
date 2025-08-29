from collections import deque

def bfs(matrix, start, goal):
    n = len(matrix) 
    
    queue = deque([[start]])  
    
    while queue:
        path = queue.popleft()  
        node = path[-1]  

       
        if node == goal:
            print("Path found:", path)
            return path
        
       
        for neighbor in range(n):
            if matrix[node][neighbor] == 1 and neighbor not in path: 
                new_path = list(path) 
                new_path.append(neighbor) 
                queue.append(new_path) 
        
        print("Queue contents:", list(queue))
        print("Number of paths in the queue:", len(queue))

matrix = [
    [0, 1, 1, 0, 0],  
    [1, 0, 1, 1, 1], 
    [1, 1, 0, 0, 1],  
    [0, 1, 0, 0, 1], 
    [0, 1, 1, 1, 0]  
]

bfs(matrix, 1, 4)