"""
Problem:
Eva recently discovered a shelf full of bottles of wine in the cellar. She counted 24 bottles of Rioja and 17 bottles of Malbec.
She also noticed the price labels on the bottles: The price of one bottle of Rioja was 25 Euro, and one bottle of Malbec costs 49 Euro.
Suddenly, she realized that her husband has spent 2000 Euro a week ago for just this wine. How many bottles did the husband already drink?
"""
import gurobipy as grb

def drunken_husband():
    """
    Solve the initial problem of the drunken husband using Gurobi.
    """
    # MODEL
    # create a gurobi model for the probelm
    model = grb.Model("drunken_husband")
    model.setParam("OutputFlag", 0)  # suppress the output log from gurobi
    
    # VARIABLES
    # let x = rioja, and y = malbec be our decision variables
    # both x, and y will be integer variables
    # we have to mark their lower bound as respective remaining bottles, this is because, we know he must have purchased >= remaining amount of those bottles
    x = model.addVar(name="rioja_bottles", vtype=grb.GRB.INTEGER, lb=24)
    y = model.addVar(name="malbec_bottles", vtype=grb.GRB.INTEGER, lb=17)
    
    # CONSTRAINTS
    # the total price of all purchased bottles cannot increase 2000 euro
    model.addConstr(25 * x + 49 * y == 2000)
    
    # OBJECTIVE
    # we want to maximize the number of bottles he purchased
    obj_func = 25 * x + 49 * y
    model.setObjective(obj_func, grb.GRB.MAXIMIZE)
    
    # OPTIMIZE
    model.optimize()
    
    # now, we check if a feasible solution was found
    if model.Status == grb.GRB.OPTIMAL:
        print("Optimal solution achieved")
        print("Optimal Objective Value", model.ObjVal)
        # get the values of the variables 
        rioja_bottles = x.X
        malbec_bottles = y.X
        bottles_already_consumed = rioja_bottles - 24 + malbec_bottles - 17
        print(f"The husband already consumed {bottles_already_consumed} bottles of wine.")
    else:
        print("No feasible solution found.")

def qs_1():
    model = grb.Model("drunken_husband")
    model.setParam("OutputFlag", 0)  # suppress the output log from gurobi
    
    x = model.addVar(name="rioja_bottles", vtype=grb.GRB.INTEGER, ub=30)
    y = model.addVar(name="malbec_bottles", vtype=grb.GRB.INTEGER, lb=17)
    
    model.addConstr(25 * x + 49 * y == 2000)
    
    obj_func = 25 * x + 49 * y
    model.setObjective(obj_func, grb.GRB.MAXIMIZE)
    
    model.optimize()
    
    if model.Status == grb.GRB.OPTIMAL:
        print("Optimal solution achieved", model.ObjVal)
    else:
        print("No feasible solution found.")

def qs_2():
    model = grb.Model("drunken_husband")
    # model.setParam("OutputFlag", 0)  # suppress the output log from gurobi
    
    x = model.addVar(name="rioja_bottles", vtype=grb.GRB.INTEGER, lb=0)
    y = model.addVar(name="malbec_bottles", vtype=grb.GRB.INTEGER, lb=0)
    
    model.addConstr(25 * x + 49 * y <= 2000)
    
    obj_func = 25 * x + 49 * y
    model.setObjective(obj_func, grb.GRB.MAXIMIZE)
    
    model.optimize()
    
    if model.Status == grb.GRB.OPTIMAL:
        print("Optimal solution achieved", model.ObjVal)
    else:
        print("No feasible solution found.")

def qs_3():
    model = grb.Model("drunken_husband")
    model.setParam("OutputFlag", 0)  # suppress the output log from gurobi
    
    x = model.addVar(name="rioja_bottles", vtype=grb.GRB.INTEGER, lb=0)
    y = model.addVar(name="malbec_bottles", vtype=grb.GRB.INTEGER, lb=0)
    
    model.addConstr(25 * x + 49 * y <= 333)
    model.addConstr(x == y)
    
    obj_func = 25 * x + 49 * y
    model.setObjective(obj_func, grb.GRB.MAXIMIZE)
    
    model.optimize()
    
    if model.Status == grb.GRB.OPTIMAL:
        print("Optimal solution achieved", model.ObjVal)
    else:
        print("No feasible solution found.")

def qs_4():
    model = grb.Model("drunken_husband")
    # model.setParam("OutputFlag", 0)  # suppress the output log from gurobi
    
    x = model.addVar(name="rioja_bottles", vtype=grb.GRB.INTEGER, lb=0)
    y = model.addVar(name="malbec_bottles", vtype=grb.GRB.INTEGER, lb=0)
    
    model.addConstr(25 * x + 49 * y <= 997)
    
    obj_func = x + y
    model.setObjective(obj_func, grb.GRB.MAXIMIZE)
    
    model.optimize()
    
    if model.Status == grb.GRB.OPTIMAL:
        print("Optimal solution achieved", model.ObjVal)
    else:
        print("No feasible solution found.")



drunken_husband()
# qs_1()
# qs_2()
# qs_3()
# qs_4()