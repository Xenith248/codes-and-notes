import networkx as nx
import matplotlib.pyplot as plt

# Create a directed multigraph
knowledge_base = nx.MultiDiGraph()

# Add nodes (concepts/entities)
knowledge_base.add_nodes_from(["Animal", "Dog", "Fur", "Bark", "Cat"])

# Add edges (relationships) with types
knowledge_base.add_edge("Dog", "Animal", relation="is_a")
knowledge_base.add_edge("Dog", "Fur", relation="has")
knowledge_base.add_edge("Dog", "Bark", relation="can")
knowledge_base.add_edge("Cat", "Animal", relation="is_a")
knowledge_base.add_edge("Cat", "Fur", relation="has")

# Add edges with attributes
knowledge_base.add_edge("Dog", "Animal", relation="inherits", confidence=0.9)
knowledge_base.add_edge("Cat", "Animal", relation="inherits", confidence=0.8)

# Visualize the knowledge base
pos = nx.spring_layout(knowledge_base)  # Positioning
plt.figure(figsize=(10, 7))
nx.draw(knowledge_base, pos, with_labels=True, node_color="lightblue", font_weight="bold", node_size=2000)

# Display edge labels with relationships and attributes
edge_labels = {(u, v): d["relation"] for u, v, d in knowledge_base.edges(data=True)}
nx.draw_networkx_edge_labels(knowledge_base, pos, edge_labels=edge_labels)

plt.title("Knowledge Base Multigraph")
plt.show()
