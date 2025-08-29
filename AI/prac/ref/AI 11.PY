# Function to parse rules and return the antecedent and consequent of each rule
def parse_rule(rule):
    # Each rule is of the form "IF <condition> THEN <variable>"
    if rule.startswith("IF"):
        condition = rule[3:rule.index("THEN")].strip()
        consequent = rule[rule.index("THEN") + 5:].strip()
        return condition, consequent
    return None, None

# Function to evaluate the Boolean condition based on the facts
def evaluate_condition(condition, facts):
    # Split the condition into parts
    parts = condition.split()
    
    # Start with the first variable's value
    result = facts[parts[0]] if parts[0] in facts else None
    
    # Process the remaining parts
    i = 1
    while i < len(parts):
        operator = parts[i]
        variable = parts[i + 1]
        
        if operator == "AND":
            result = result and (facts[variable] if variable in facts else None)
        elif operator == "OR":
            result = result or (facts[variable] if variable in facts else None)
        elif operator == "NOT":
            result = not (facts[variable] if variable in facts else None)
        
        i += 2
    
    return result

# Recursive function to apply Modus Tollens and satisfy goals
def infer_goal(goal, facts, rules, visited_goals):
    # Check if the goal is already satisfied or visited
    if goal in facts:
        print(f"Goal {goal} is already satisfied with value {facts[goal]}")
        return facts
    if goal in visited_goals:
        print(f"Goal {goal} has already been visited, returning.")
        return facts
    
    # Mark goal as visited to avoid infinite recursion
    visited_goals.add(goal)
    
    # Find rule with this goal as consequent
    for rule in rules:
        condition, consequent = parse_rule(rule)
        if consequent == goal:
            print(f"Found rule: IF {condition} THEN {goal}")
            # Evaluate the condition
            if evaluate_condition(condition, facts):
                print(f"Condition '{condition}' is satisfied, goal '{goal}' is inferred!")
                facts[goal] = True
                return facts
            else:
                print(f"Condition '{condition}' is not satisfied. Inferring additional goals.")
                # If condition is not satisfied, break it down and infer additional goals
                sub_goals = condition.split()[::2]  # Get all variable names in the condition
                for sub_goal in sub_goals:
                    if sub_goal not in facts:
                        facts = infer_goal(sub_goal, facts, rules, visited_goals)
                
    return facts

# Main function to run the inference engine
def run_inference_engine():
    # Input the number of variables (min 4, max 26)
    num_variables = int(input("Enter the number of variables (4-26): "))
    
    # Input the variable names
    variables = input("Enter the variable names (space-separated): ").split()
    
    # Input five rules
    rules = []
    print("Enter 5 rules in the format 'IF <condition> THEN <variable>':")
    for _ in range(5):
        rule = input()
        rules.append(rule)
    
    # Input the Goal
    goal = input("Enter the goal variable (one of the variables): ")
    
    # Input two facts (variable name and truth value)
    facts = {}
    for _ in range(2):
        var, value = input("Enter a fact (variable and value): ").split()
        facts[var] = value == 'T'  # 'T' means True, 'F' means False
    
    # Run the inference engine
    visited_goals = set()  # Track visited goals to avoid infinite recursion
    facts = infer_goal(goal, facts, rules, visited_goals)
    
    # Output the final facts
    print("Final facts:", facts)

# Run the inference engine
run_inference_engine()

