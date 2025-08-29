class Graph:

    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = []

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    def printArr(self, dist):
        print("Vertex Distance from Source")
        for i in range(self.V):
            print("{0}\t\t{1}".format(i, dist[i]))

    def BellmanFord(self, src):
        dist = [float("-Inf")] * self.V  # Change initialization to negative infinity
        dist[src] = 0
        for _ in range(self.V - 1):
            for u, v, w in self.graph:
                if dist[u] != float("-Inf") and dist[u] + w > dist[v]:  # Change the condition
                    dist[v] = dist[u] + w
        for u, v, w in self.graph:
            if dist[u] != float("-Inf") and dist[u] + w > dist[v]:  # Change the condition
                print("Graph contains positive weight cycle")  # Change the message
                return

        self.printArr(dist)

if __name__ == '__main__':
	g = Graph(5)
	g.addEdge(0, 1, 1)
	g.addEdge(0, 2, 4)
	g.addEdge(1, 2, 3)
	g.addEdge(1, 3, 2)
	g.addEdge(1, 4, 2)
	g.addEdge(2, 3, 5)
	g.addEdge(4, 3, 3)
    
g.BellmanFord(0)
