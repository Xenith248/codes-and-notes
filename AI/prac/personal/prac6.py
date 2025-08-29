from collections import defaultdict

class CSP:
    def __init__(self, variables, domains):
        self.variables = variables  # List of variables
        self.domains = {var: list(domains) for var in variables}  # Domains
        self.constraints = defaultdict(list)  # Constraints dictionary

    def add_constraint(self, var1, var2):
        """Add a binary constraint that var1 != var2."""
        self.constraints[var1].append(var2)
        self.constraints[var2].append(var1)

    def is_consistent(self, var, value, assignment):
        """Check if assigning value to var satisfies all constraints."""
        for neighbor in self.constraints[var]:
            if neighbor in assignment and assignment[neighbor] == value:
                return False
        return True

    def backtrack(self, assignment={}):
        """Backtracking search."""
        if len(assignment) == len(self.variables):
            return assignment  # All variables assigned
        
        unassigned = [v for v in self.variables if v not in assignment]
        var = unassigned[0]  # Choose the first unassigned variable (can use heuristics)

        for value in self.domains[var]:
            if self.is_consistent(var, value, assignment):
                assignment[var] = value  # Assign value
                result = self.backtrack(assignment)
                if result:
                    return result
                del assignment[var]  # Backtrack
        
        return None

# Example: Map Coloring
variables = ["WA", "NT", "SA", "Q", "NSW", "V", "T"]
domains = ["Red", "Green", "Blue"]
csp = CSP(variables, domains)

# Add constraints (adjacent regions cannot have the same color)
edges = [("WA", "NT"), ("WA", "SA"), ("NT", "SA"), ("NT", "Q"),
         ("SA", "Q"), ("SA", "NSW"), ("SA", "V"), ("Q", "NSW"), ("NSW", "V")]
for var1, var2 in edges:
    csp.add_constraint(var1, var2)

solution = csp.backtrack()
print("Solution:", solution)
