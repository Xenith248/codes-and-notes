class SimpleInferenceEngine:
    def __init__(self):
        self.knowledge_base = set()  # Known facts
        self.rules = []  # List of rules in the form (premise, conclusion)

    def add_fact(self, fact):
        """Add a fact to the knowledge base."""
        self.knowledge_base.add(fact)

    def add_rule(self, premise, conclusion):
        """Add a rule in the form premise → conclusion."""
        self.rules.append((premise, conclusion))

    def infer(self):
        """Perform inference using Modus Ponens and Modus Tollens."""
        new_inferences = set()
        for premise, conclusion in self.rules:
            # Modus Ponens: If premise is true, infer conclusion
            if premise in self.knowledge_base and conclusion not in self.knowledge_base:
                new_inferences.add(conclusion)

            # Modus Tollens: If ¬conclusion is true, infer ¬premise
            if f"¬{conclusion}" in self.knowledge_base and f"¬{premise}" not in self.knowledge_base:
                new_inferences.add(f"¬{premise}")
        
        # Add new inferences to the knowledge base
        self.knowledge_base.update(new_inferences)
        return new_inferences

    def run_inference(self):
        """Iteratively apply inference until no new facts can be derived."""
        while True:
            new_inferences = self.infer()
            if not new_inferences:
                break

# Example usage
engine = SimpleInferenceEngine()

# Adding rules
engine.add_rule("It_rains", "Streets_wet")  # It_rains → Streets_wet
engine.add_rule("Lights_on", "Room_bright") # Lights_on → Room_bright

# Adding facts
engine.add_fact("It_rains")         # It_rains is true
engine.add_fact("¬Streets_wet")     # Streets_wet is false (¬Streets_wet)

# Run inference
engine.run_inference()

# Print results
print("Knowledge Base:", engine.knowledge_base)
