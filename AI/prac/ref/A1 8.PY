import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict, deque

class MultiGraph:
    def __init__(self):
        # use DICT TO STORE EDGES
        self.graph = defaultdict(lambda: defaultdict(list))
    
    # ADDS EDGE AS A LABEL
    def add_edge(self, from_node, to_node, relation):
        self.graph[from_node][relation].append(to_node)
    
    # CHECK FOR PATH BW 2 NODES
    def has_path(self, start, end):
        visited = set()
        queue = deque([start])
        
        while queue:
            node = queue.popleft()
            if node == end:
                return True
            if node not in visited:
                visited.add(node)
                # ALL NEUGH IRRESP OF RELATIONSHIP
                for relations in self.graph[node].values():
                    queue.extend(relations)
        return False

    # VISUALIZE USIN NETWORKX
    def visualize(self):
        G = nx.MultiDiGraph()  
        
        # ADD NODES N EDGES FROM DICTIONARY
        for from_node, relations in self.graph.items():
            for relation, to_nodes in relations.items():
                for to_node in to_nodes:
                    G.add_edge(from_node, to_node, label=relation)
        
        # DRAW GRAPH
        pos = nx.spring_layout(G)
        plt.figure(figsize=(10, 7))
        
        # NODES AND EDGES

        nx.draw(G, pos, with_labels=True, node_color="yellow", font_size=10, node_size=2000, edge_color="pink", arrows=True)
        
        # DIFF relationships HAVE DIFF LABELS
        edge_labels = {(u, v): data['label'] for u, v, data in G.edges(data=True)}
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='purple')
        
        plt.show()

# Ex
knowledge_base = MultiGraph()

# EDGES= RELATIONSHIP
knowledge_base.add_edge("Alice", "teacher", "is a")
knowledge_base.add_edge("teachers", "schools", "work in")
knowledge_base.add_edge("schools", "places", "are")
knowledge_base.add_edge("children", "schools", "learn")
knowledge_base.add_edge("Alice", "children", "enjoys teaching")
knowledge_base.add_edge("teachers", "responsibility", "have a")
knowledge_base.add_edge("responsibility", "students", "to guide")
knowledge_base.add_edge("students", "style", "appreciate")

# PATHDS
print("Path from Alice to style:", knowledge_base.has_path("Alice", "style"))  # MUST BE True
print("Path from style to Alice:", knowledge_base.has_path("style", "Alice"))  # NO TRUE SO False


knowledge_base.visualize()

