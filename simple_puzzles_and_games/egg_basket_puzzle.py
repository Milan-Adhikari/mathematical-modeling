"""
Problem:
A woman has been carrying a basket of eggs to the market when a passer-by bumped into her. She dropped the basket and all the eggs were broken.
The passer-by wishing to pay for her loss, asked, "How many eggs were in your basket?" "I do not remember exactly", the woman replied ,"
but I do recall that when I divided the number of eggs by 2, 3, 4, 5 or 6 there was always one egg left over. When I took the eggs out in 
groups of seven, I emptied the basket." What is the smallest possible number of eggs that broke?
"""
import gurobipy as grb

def egg_basekt():
    model = grb.Model("egg_basket")
    
    # Variables
    x = model.addVar(name="number_of_eggs", vtype=grb.GRB.INTEGER, lb=1)
    # variable for each val
    vals = [2, 3, 4, 5, 6, 7]
    for val in vals:
        model.addVar(name=f'q_{val}', vtype=grb.GRB.INTEGER, lb=0)
    model.update()
    
    # add constraint
    # for each val 2, 3, 4, 5, 6, when the number of eggs is divided by it, the remainder must be 1
    # the remainder when divided by 7 is 0
    for val in vals:
        quot = model.getVarByName(f'q_{val}')
        rem = 0 if val == 7 else 1
        model.addConstr(x - (val * quot) == rem)
    
    # objective: find the least number of eggs that could have been broken
    model.setObjective(x, grb.GRB.MINIMIZE)
    
    model.optimize()
    
    if model.Status == grb.GRB.OPTIMAL:
        print("Optimal solution found", model.ObjVal)
    else:
        print("No Feasible solution")
        

egg_basekt()