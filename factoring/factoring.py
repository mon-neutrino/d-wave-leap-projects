import dwavebinarycsp as dbc

and_gate = dbc.factories.and_gate(["x1", "x2", "x3"])
and_csp = dbc.ConstraintSatisfactionProblem('BINARY')
and_csp.add_constraint(and_gate)

# Test the CSP
and_csp.check({"x1": 1, "x2": 1, "x3": 1})
