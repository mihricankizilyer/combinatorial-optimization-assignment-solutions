from pulp import *

# Descirbe Variables
"""
x11: 1.kardeşin aldığı dolu kavonoz
x12: 1.kardeşin aldığı yarı dolu kavonoz
x13: 1.kardeşin aldığı boş kavonoz
x21: 2.kardeşin aldığı dolu kavonoz
x22: 2.kardeşin aldığı yarı dolu kavonoz
x23: 2.kardeşin aldığı boş kavonoz
x31: 3.kardeşin aldığı dolu kavonoz
x32: 3.kardeşin aldığı yarı dolu kavonoz
x33: 3.kardeşin aldığı boş kavonoz
"""

# 1. Initialize Model
model = LpProblem("min",LpMinimize)

# 2. Define Variables
x11 = LpVariable("x11", lowBound = 0, cat = "Integer")
x12 = LpVariable("x12", lowBound = 0, cat = "Integer")
x13 = LpVariable("x13", lowBound = 0, cat = "Integer")
x21 = LpVariable("x21", lowBound = 0, cat = "Integer")
x22 = LpVariable("x22", lowBound = 0, cat = "Integer")
x23 = LpVariable("x23", lowBound = 0, cat = "Integer")
x31 = LpVariable("x31", lowBound = 0, cat = "Integer")
x32 = LpVariable("x32", lowBound = 0, cat = "Integer")
x33 = LpVariable("x33", lowBound = 0, cat = "Integer")

# 4. Define Constraints
model += x11 + x12 + x13 == 7
model += x21 + x22 + x23 == 7
model += x31 + x32 + x33 == 7

model += x11 + 0.5 * x12 == x12 + x22 * 0.5
model += x11 + 0.5 * x12 == x31 + x32 * 0.5
model += x21 + 0.5 * x22 == x31 + x32 * 0.5

model += x11 + x21 + x31 == 7
model += x12 + x22 + x32 == 7
model += x13 + x23 + x33 == 7

# 5. Solve Model
model.solve()
print("1.kardeşin aldığı dolu kavonoz: {}".format(x11.varValue))
print("1.kardeşin aldığı yarı dolu kavonoz: {}".format(x12.varValue))
print("1.kardeşin aldığı boş kavonoz: {}".format(x13.varValue))
print("2.kardeşin aldığı dolu kavonoz: {}".format(x21.varValue))
print("2.kardeşin aldığı yarı dolu kavonoz: {}".format(x22.varValue))
print("2.kardeşin aldığı boş kavonoz: {}".format(x23.varValue))
print("3.kardeşin aldığı dolu kavonoz: {}".format(x31.varValue))
print("3.kardeşin aldığı yarı dolu kavonoz: {}".format(x32.varValue))
print("3.kardeşin aldığı boş kavonoz: {}".format(x33.varValue))