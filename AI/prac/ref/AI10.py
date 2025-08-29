from sympy.logic.boolalg import And, Or, Not
from sympy.abc import A, B, C

# boolean exp for LHS AND RHS
lhs = Or(And(A, B), And(B, Not(C)), And(A, C))
rhs = Or(And(A, C), And(B, Not(C)))

# LHS
simplified_lhs = lhs.simplify()

#IF LHS and RHS are equivalent
equivalence = simplified_lhs.equals(rhs)

#RESULT
print("Original LHS:", lhs)
print("Simplified LHS:", simplified_lhs)
print("RHS:", rhs)
print("Are LHS and RHS equivalent?", equivalence)
