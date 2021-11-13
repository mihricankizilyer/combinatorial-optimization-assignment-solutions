from pulp import *

# Descirbe Variables
"""
x1: Ev Kredisi Tip 1
x2: Ev Kredisi Tip 2
x3: Araç Kredisi
x4: Tüketici Kredisi
"""

# 1. Initialize Model
model = LpProblem("max_kar",LpMaximize)

# 2. Define Variables
x1 = LpVariable("x1", lowBound = 0, cat = "Integer")
x2 = LpVariable("x2", lowBound = 0, cat = "Integer")
x3 = LpVariable("x3", lowBound = 0, cat = "Integer")
x4 = LpVariable("x4", lowBound = 0, cat = "Integer")

# 3. Define Objective Function
model += 0.14*x1 + 0.2*x2 + 0.2*x3 + 0.1*x4

# 4. Define Constraints
model += x1 + x2 + x3 + x4 <= 250000000
model += x1 >= 0.55 * (x1 + x2)
model += x1 >= 0.25 * (x1 + x2 + x3 + x4)
model += x2 <= 0.25 * (x1 + x2 + x3 + x4)
model += 0.14*x1 + 0.2*x2 + 0.2*x3 + 0.1*x4 <= 0.15 * (x1 + x2 + x3 +x4)

# 5. Solve Model
model.solve()
print("Ev Kredisi Tip 1 için Ayrılan Miktar: {}".format(x1.varValue))
print("Ev Kredisi Tip 2 için Ayrılan Miktar: {}".format(x2.varValue))
print("Araç Kredisi için Ayrılan Miktar: {}".format(x3.varValue))
print("Tüketici Kredisi için Ayrılan Miktar {}".format(x4.varValue))


