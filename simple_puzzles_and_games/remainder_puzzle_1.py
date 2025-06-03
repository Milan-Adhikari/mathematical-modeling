"""
Problem:
Is there a number which gives a remainder of 1 when divided by 3, and a remainder of 2 when divided by 4, and a remainder of 3 when divided by 5 and
finally a remainder of 4 when divided by 6? Find the smallest such number, if any exists.
"""
import gurobipy as grb

def remainder_puzzle_1():
    model = grb.Model("remainder_puzzle_1")
    
    # VARIABLES
    x = model.addVar(name="number", vtype=grb.GRB.INTEGER, lb=0)
    values = [3, 4, 5, 6]
    # CONSTRAINTS
    for val in values:
        model.addVar(name=f'q_{val}', vtype=grb.GRB.INTEGER, lb=0)
        model.update()
        # adding constraints here to minimize the loops
        model.addConstr(x - (model.getVarByName(f'q_{val}') * val) == val - 2)
        
    # OBJECTIVE
    model.setObjective(x, grb.GRB.MINIMIZE)
    
    # OPTIMIZE
    model.optimize()
    
    if model.Status == grb.GRB.OPTIMAL:
        print("Optimal result: ", model.ObjVal)
    else:
        print("No feasible solution found")

remainder_puzzle_1()