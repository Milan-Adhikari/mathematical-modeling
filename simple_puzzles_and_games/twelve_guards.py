"""
Problem:
The castle of Lord Hamilton is threatened from all four sides. Therefore he places 12 guards on the top of its highest tower to observe the surroundings 
day and night. The guards can be placed on 12 platforms ( the positions are numbered from 1 to 12) - at each side there are 4 positions. 
Guards on a side platform can look only in one of four directions, guards on the corner platforms 1, 4, 9, and 12 can look at two sides. 
Hence, the corner platform belongs to 2 sides. The problem is to place the guards in such a way that there are 5 guards observing each side. 
How should they be arranged on the different platforms?
"""
import gurobipy as grb
from itertools import combinations

def twelve_guards():
    model = grb.Model("twelve_guards")
    model.setParam("OutputFlag", 0)
    
    # VARIABLES
    # we do not need to model the guards into variables, because it does not matter which guard is placed on which platform
    # the main point of concern is about how many guards need to be placed in each platform, and therefore we create a variable for each platform
    platform_variables = []
    for i in range(1, 13):
        # we can put 0 guards or upto 5 guards. We can put more, but it is not necessary
        v = model.addVar(name=f'platform_{i}', vtype=grb.GRB.INTEGER, lb=0, ub=5)
        platform_variables.append(v)
    model.update()
    # CONSTRAINTS
    # the total number of guards available are only 12, and we want to place all of them on the platforms
    model.addConstr(grb.quicksum(platform_variables) == 12)
    # or we can also directly do
    # model.addConstr(grb.quicksum(model.getVarByName(f'platform_{i}') for i in range(1, 13)))
    
    # for each side, we need to have 5 guards observing it
    sides = [[1, 2, 3, 4], [4, 6, 8, 12], [12, 11, 10, 9], [9, 7, 5, 1]]
    for side in sides:
        model.addConstr(grb.quicksum([model.getVarByName(f'platform_{i}') for i in side]) == 5)
    
    # # constraint for qs. 2
    # for var in platform_variables:
    #     model.addConstr(var <= 2)
    
    # # for qs. 4
    # z = model.addVar(name="max_load_per_platform", vtype=grb.GRB.INTEGER, lb=0, ub=5)
    # model.update
    
    # for var in platform_variables:
    #     model.addConstr(var <= z)
    
    # model.setObjective(z, grb.GRB.MINIMIZE)
        
    # OPTIMIZE
    model.optimize()
    
    if model.Status == grb.GRB.OPTIMAL:
        print("Optimal Solution Found")
        for var in model.getVars():
            print(f'{var.VarName}: ', abs(var.X))
    else:
        print("No feasible solution found")

twelve_guards()