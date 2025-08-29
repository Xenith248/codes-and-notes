import networkx as nx
import matplotlib.pyplot as plt

def draw_csp_graph(variables, binary_constraints, domains, title="CSP Constraint Graph"):
    """
    Draw the constraint graph corresponding to the given CSP problem.
    Each variable is a node, and each binary constraint creates an edge.
    """
    G = nx.Graph()
    
    # Add nodes with their domains
    for var in variables:
        G.add_node(var, label=f"{var}: {domains[var]}")
    
    # Add edges for binary constraints
    for (var1, _, var2, _, _) in binary_constraints:
        G.add_edge(var1, var2)
    
    # Extract node labels for visualization
    labels = nx.get_node_attributes(G, 'label')
    
    
    plt.figure(figsize=(8, 6))
    nx.draw(G, with_labels=True, labels=labels, node_color='lightblue', font_weight='bold')
    plt.title(title)
    plt.show()


    # AN EXAMPLE
def main():

    variables = ['A', 'B', 'C']
    domains = {'A': {1, 2, 3, 4, 5}, 'B': {2, 3, 4, 5}, 'C': {1, 3, 5}}
    binary_constraints = [
        ('A', '>', 'B', '+', 1),  
        ('B', '<', 'C', '+', 2)   
    ]
    
  
    draw_csp_graph(variables, binary_constraints, domains, title="CSP Constraint Graph")

main()
