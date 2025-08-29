class InferenceEngine:
    def __init__(self):
        self.rules = []  # List of (P, Q) tuples representing P → Q
        self.knowledge_base = set()  # Set of known facts (positive or negative)

    def add_rule(self, premise, conclusion):
        self.rules.append((premise, conclusion))

    def add_fact(self, fact):
        self.knowledge_base.add(fact)

    def apply_modus_tollens(self):
        new_inferences = set()
        for premise, conclusion in self.rules:
            if f"¬{conclusion}" in self.knowledge_base:  # ¬Q
                new_inferences.add(f"¬{premise}")  # ¬P
        self.knowledge_base.update(new_inferences)
        return new_inferences
# Example usage
engine = InferenceEngine()
engine.add_rule("It_rains", "Streets_wet")  # P → Q
engine.add_fact("¬Streets_wet")            # ¬Q

inferred = engine.apply_modus_tollens()
print("Inferred Facts:", inferred)         # Should infer ¬It_rains