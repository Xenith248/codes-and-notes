import networkx as nx
import matplotlib.pyplot as plt

# Create directed graph
G = nx.DiGraph()

# Add nodes for entities and actions (verbs reified as separate nodes)
entities = ["Jerry", "cat", "mammals", "animals", "mortal", "legs", "milk"]
actions = ["is_a", "are_a", "are", "have", "like", "drink"]

# Add nodes
G.add_nodes_from(entities + actions)

# Define edges with labels
edges = [
    ("Jerry", "is_a", "subject"), ("is_a", "cat", "type"),
    ("Cats", "are_a", "subject"), ("are_a", "mammals", "type"),
    ("Mammals", "are_a", "subject"), ("are_a", "animals", "type"),
    ("Animals", "are", "subject"), ("are", "mortal", "type"),
    ("Cats", "have", "subject"), ("have", "legs", "object"),
    ("Cats", "like", "subject"), ("like", "milk", "object"),
    ("like", "drink", "action"), ("drink", "milk", "object")
]

# Add edges to the graph with labels
for from_node, to_node, label in edges:
    G.add_edge(from_node, to_node, label=label)

# Draw the graph
pos = nx.spring_layout(G)
plt.figure(figsize=(12, 8))
nx.draw(G, pos, with_labels=True, node_color="lightblue", font_size=10, node_size=2000, edge_color="gray", arrows=True)

# Draw edge labels for roles
edge_labels = {(u, v): data['label'] for u, v, data in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

plt.show()
