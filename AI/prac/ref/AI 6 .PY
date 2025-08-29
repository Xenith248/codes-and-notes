import matplotlib.pyplot as plt
import networkx as nx

class CSP:
    def __init__(self):
        self.variables = {}
        self.unary_constraints = []
        self.binary_constraints = []
        self.graph = nx.Graph()

    def read_input(self):
        # Read number of variables
        N_V = int(input("Enter the number of variables: "))
        
        # Read variable names and domains
        for _ in range(N_V):
            var_name = input("Enter variable name: ")
            domain = list(map(int, input(f"Enter domain for {var_name} (space-separated): ").split()))
            self.variables[var_name] = domain
            self.graph.add_node(var_name)

        # Read unary constraints
        N_UC = int(input("Enter the number of unary constraints: "))
        for _ in range(N_UC):
            constraint = input("Enter unary constraint (e.g., A < 5): ")
            self.unary_constraints.append(constraint)

        # Read binary constraints
        N_BC = int(input("Enter the number of binary constraints: "))
        for _ in range(N_BC):
            constraint = input("Enter binary constraint (e.g., A < B + 5): ")
            self.binary_constraints.append(constraint)

    def apply_unary_constraints(self):
        for constraint in self.unary_constraints:
            var, operator, value = constraint.split()
            value = int(value)
            if operator == "<":
                self.variables[var] = [v for v in self.variables[var] if v < value]
            elif operator == ">":
                self.variables[var] = [v for v in self.variables[var] if v > value]
            elif operator == "=":
                self.variables[var] = [v for v in self.variables[var] if v == value]
            print(f"Domain of {var} after unary constraint: {self.variables[var]}")

    def apply_binary_constraints(self):
        for constraint in self.binary_constraints:
            parts = constraint.split()
            var1, operator, var2, arith_op, constant = parts[0], parts[1], parts[2], parts[3], int(parts[4])

            # Adjust domain of var1 based on var2's domain
            if operator == ">":
                if arith_op == "+":
                    for value2 in self.variables[var2]:
                        for value1 in list(self.variables[var1]):
                            if value1 <= value2 + constant:
                                self.variables[var1].remove(value1)

            print(f"Domain of {var1} after binary constraint: {self.variables[var1]}")
            print(f"Domain of {var2} remains: {self.variables[var2]}")

    def draw_graph(self):
        # Add edges for binary constraints
        for constraint in self.binary_constraints:
            parts = constraint.split()
            var1, _, var2, _, _ = parts
            self.graph.add_edge(var1, var2)

        # Draw the graph with the updated domains
        pos = nx.spring_layout(self.graph)  # Positioning of nodes in the graph
        nx.draw(self.graph, pos, with_labels=True, node_color='lightblue', node_size=3000, font_size=12)

        # Add labels with the domains
        labels = {node: f"{node}: {str(self.variables[node])}" for node in self.graph.nodes}
        nx.draw_networkx_labels(self.graph, pos, labels=labels, font_size=10)

        # Display the graph
        plt.title("Constraint Graph with Variable Domains")
        plt.show()

    def run(self):
        self.read_input()
        self.apply_unary_constraints()
        self.apply_binary_constraints()
        self.draw_graph()

# Initialize and run the CSP solver
csp = CSP()
csp.run()

