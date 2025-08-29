import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

'''
Jerry is a cat.
 Jerry was sitting on the sofa.
 Jerry is owned by Tom.
 Tom called Jerry.
 Jerry walked from the sofa to Tom.
 Tom gave some milk to Jerry.
 Jerry drank the milk
'''

relationships = [
    ("Jerry", "cat", "is a"),
    ("Jerry", "sofa", "sitting"),
    ("Jerry", "Tom", "owned"),
    ("tom", "jerry", "Called"),
    ("jerry", "Tom", "Walked"),
    ("Tom", "jerry", "Gave"),
    ("Jerry","milk","drank")
]

for start, end, relation in relationships:
    G.add_edge(start, end, label=relation)

pos = nx.spring_layout(G)  
nx.draw(G, pos, with_labels=True, node_size=300, node_color="skyblue", font_size=10, font_weight="bold", arrowsize=20)

edge_labels = nx.get_edge_attributes(G, 'label')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=9, label_pos=0.5)

plt.title("Knowledge Graph of Relationships")
plt.show()