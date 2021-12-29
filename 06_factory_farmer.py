from pulp import *

# Descirbe Variables
"""
x11: 1.çiftçiden 1.bankaya giden miktar
x21: 2.çiftçiden 1.bankaya giden miktar
x31: 3.çiftçiden 1.bankaya giden miktar
x12: 1.çiftçiden 2.bankaya giden miktar
x22: 2.çiftçiden 2.bankaya giden miktar
x32: 3.çiftçiden 2.bankaya giden miktar
"""

# 1. Initialize Model
model = LpProblem("max_kar",LpMaximize)

# 2. Define Variables
x11 = LpVariable("x11", lowBound = 0, cat = "Integer")
x21 = LpVariable("x21", lowBound = 0, cat = "Integer")
x31 = LpVariable("x31", lowBound = 0, cat = "Integer")
x12 = LpVariable("x12", lowBound = 0, cat = "Integer")
x22 = LpVariable("x22", lowBound = 0, cat = "Integer")
x32 = LpVariable("x32", lowBound = 0, cat = "Integer")

# 3. Define Objective Function
model += 50*(x11 + x21 + x31 + x12 + x22 + x32) - 11*(x11 + x12) - 10*(x21 + x22) - 9*(x31 + x32) \
- 3*x11 - 3.5*x12 - 2*x21 - 2.5*x22 - 6*x31 - 4*x32- 26*(x11 + x21 + x31) -21*(x12 + x22 + x32)

# 4. Define Constraints
model += x11 + x12 <= 200
model += x21 + x22 <= 310
model += x31 + x32 <= 420
model += x11 + x21 + x31 <= 460
model += x12 + x22 + x32 <= 560

# 5. Solve Model
model.solve()
print("1.çiftçiden 1.bankaya giden miktar: {}".format(x11.varValue))
print("2.çiftçiden 1.bankaya giden miktar {}".format(x21.varValue))
print("3.çiftçiden 1.bankaya giden miktar: {}".format(x31.varValue))
print("1.çiftçiden 2.bankaya giden miktar {}".format(x12.varValue))
print("2.çiftçiden 2.bankaya giden miktar: {}".format(x22.varValue))
print("3.çiftçiden 2.bankaya giden miktar {}".format(x32.varValue))
