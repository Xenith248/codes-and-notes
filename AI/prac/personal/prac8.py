import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph
semantic_net = nx.DiGraph()

# Add nodes (concepts)
semantic_net.add_nodes_from(["Animal", "Dog", "Fur", "Bark"])

# Add edges (relationships)
semantic_net.add_edge("Dog", "Animal", relation="is_a")
semantic_net.add_edge("Dog", "Fur", relation="has")
semantic_net.add_edge("Dog", "Bark", relation="can")

# Visualize the semantic net
pos = nx.spring_layout(semantic_net)
nx.draw(semantic_net, pos, with_labels=True, node_color="lightblue", font_weight="bold")
edge_labels = nx.get_edge_attributes(semantic_net, "relation")
nx.draw_networkx_edge_labels(semantic_net, pos, edge_labels=edge_labels)
plt.show()
