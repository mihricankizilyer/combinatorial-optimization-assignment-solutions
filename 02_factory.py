from pulp import *

# 1. Initialize Model
model = LpProblem("max_kar",LpMaximize)

# 2. Define Variables
x1 = LpVariable("x1", lowBound = 0, cat = "Integer")
x2 = LpVariable("x2", lowBound = 0, cat = "Integer")
x3 = LpVariable("x3", lowBound = 0, cat = "Integer")
x4 = LpVariable("x4", lowBound = 0, cat = "Integer")
x5 = LpVariable("x5", lowBound = 0, cat = "Integer")

# 3. Define Objective Function
model += 550*x1 + 600*x2 + 350*x3 + 400*x4 + 200*x5

# 4. Define Constraints
model += 12*x1 + 20*x2 + 25*x4 + 15*x5 <= 3*6*2*8
model += 10*x1 + 8*x2 + 16*x3 <= 2*2*8*6
model += 20*x1 + 20*x2 + 20*x3 + 20*x4 + 20*x5 <= 2*8*8

# 5. Solve Model
model.solve()
print("1. ürünün üretim mikarı: {}".format(x1.varValue))
print("2. ürünün üretim miktarı {}".format(x2.varValue))
print("3. ürünün üretim mikarı: {}".format(x3.varValue))
print("4. ürünün üretim miktarı {}".format(x4.varValue))
print("5. ürünün üretim mikarı: {}".format(x5.varValue))

