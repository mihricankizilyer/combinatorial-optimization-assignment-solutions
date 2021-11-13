from pulp import *

# Descirbe Variables
"""
x1: 1. madende çalışılacak gün
x2: 2. madende çalışılacak gün
"""

# 1. Initialize Model
model = LpProblem("min_kar",LpMinimize)

# 2. Define Variables
x1 = LpVariable("x1", lowBound = 0, cat = "Integer")
x2 = LpVariable("x2", lowBound = 0, cat = "Integer")

# 3. Define Objective Function
model += 180*x1 + 160*x2

# 4. Define Constraints
model += 6*x1 + x2 >= 12
model += 3*x1 + x2 >= 8
model += 4*x1 + 6*x2 >= 24

# 5. Solve Model
model.solve()
print("1.madende çalışılacak gün: {}".format(x1.varValue))
print("2.madende çalışılacak gün {}".format(x2.varValue))