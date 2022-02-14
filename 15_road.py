from pulp import *

# Descirbe Variables
"""
x12: 1'den 2'ye en kısa yol ile gidilirse
x13: 1'den 3'e en kısa yol ile gidilirse
x24: 2'den 4'e en kısa yol ile gidilirse
x25: 2'den 5'e en kısa yol ile gidilirse
x32: 3'den 2'ye en kısa yol ile gidilirse
x34: 3'den 4'e en kısa yol ile gidilirse
x35: 3'den 5'e en kısa yol ile gidilirse
x45: 4'den 5'e en kısa yol ile gidilirse
x46: 4'den 6'ya en kısa yol ile gidilirse
x56: 5'den 6'ya en kısa yol ile gidilirse
"""

# 1. Initialize Model
model = LpProblem("min",LpMinimize)

# 2. Define Variables
x12 = LpVariable("x12", lowBound = 0, cat = "Binary")
x13 = LpVariable("x13", lowBound = 0, cat = "Binary")
x24 = LpVariable("x24", lowBound = 0, cat = "Binary")
x25 = LpVariable("x25", lowBound = 0, cat = "Binary")
x32 = LpVariable("x32", lowBound = 0, cat = "Binary")
x34 = LpVariable("x34", lowBound = 0, cat = "Binary")
x35 = LpVariable("x35", lowBound = 0, cat = "Binary")
x45 = LpVariable("x45", lowBound = 0, cat = "Binary")
x46 = LpVariable("x46", lowBound = 0, cat = "Binary")
x56 = LpVariable("x56", lowBound = 0, cat = "Binary")

# 3. Define Objective Function
model += 10*x12 + 3*x13 + 2*x32 + 7*x34 + 3*x35 + 3*x25 + x24 + x45 + 7*x46 + 2*x56

# 4. Define Constraints
model += x12 + x13 == 1
model += x12 + x32 == x24 + x25
model += x24 + x34 == x45 + x46
model += x25 + x35 + x45 == x56
model += x46 + x56 == 1

# 5. Solve Model
model.solve()
print("1'den 2'ye en kısa yol ile gidilirse: {}".format(x12.varValue))
print("1'den 3'e en kısa yol ile gidilirse{}".format(x13.varValue))
print("2'den 4'e en kısa yol ile gidilirse: {}".format(x24.varValue))
print("2'den 5'e en kısa yol ile gidilirse {}".format(x25.varValue))
print("3'den 2'ye en kısa yol ile gidilirse: {}".format(x32.varValue))
print("3'den 4'e en kısa yol ile gidilirse {}".format(x34.varValue))
print("3'den 5'e en kısa yol ile gidilirse: {}".format(x35.varValue))
print("4'den 5'ya en kısa yol ile gidilirse {}".format(x45.varValue))
print("4'den 6'ya en kısa yol ile gidilirse: {}".format(x46.varValue))
print("5'den 6'ya en kısa yol ile gidilirse: {}".format(x56.varValue))


