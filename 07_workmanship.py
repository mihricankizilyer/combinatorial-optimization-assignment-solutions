from pulp import *

# Descirbe Variables
"""
x1: A ürününden satılan birim 
x2: B ürününden satılan birim 
x3: C ürününden satılan birim 
y1: A ürününden hammade olan birim
y2: B ürününden hammade olan birim
"""

# 1. Initialize Model
model = LpProblem("max_kar",LpMaximize)

# 2. Define Variables
x1 = LpVariable("x1", lowBound = 0)
x2 = LpVariable("x2", lowBound = 0)
x3 = LpVariable("x3", lowBound = 0)
y1 = LpVariable("y1", lowBound = 0)
y2 = LpVariable("y2", lowBound = 0)

# 3. Define Objective Function
model += 8 * x1 + 70 * x2 + 100 * x3

# 4. Define Constraints
model += x1 + y1 + 2 * (x2 + y2) + 3 * x3 <= 40
model += x2 + y2 == 0.5 * y1
model += x3 == y2

# 5. Solve Model
model.solve()
print("A ürününden satılan birim : {}".format(x1.varValue))
print("B ürününden satılan birim: {}".format(x2.varValue))
print("C ürününden satılan birim: {}".format(x3.varValue))
print("A ürününden hammade olan birim: {}".format(y1.varValue))
print("B ürününden hammade olan birim:  {}".format(y2.varValue))
