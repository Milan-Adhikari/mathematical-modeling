"""
Problem:
This solution is the answer to the qs. 4 from the book to the "remainder_puzzle_1".
"""
import gurobipy as grb

def remainder_puzzle_2():
    model = grb.Model("remainder_puzzle_2")
    model.setParam("OutputFlag", 0)
    
    values = [3, 4, 5, 6]
    
    previous_solution = []
    
    for _ in range(10):
        lb = 0
        if len(previous_solution) > 0:
            lb = previous_solution[-1]+1
        # VARIABLES
        x = model.addVar(name="number", vtype=grb.GRB.INTEGER, lb=lb)
    
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
            # print("Optimal result: ", model.ObjVal)
            previous_solution.append(model.ObjVal)
        else:
            print("No feasible solution found")
    
    print("10 smallest solutions are: \n", previous_solution)

remainder_puzzle_2()