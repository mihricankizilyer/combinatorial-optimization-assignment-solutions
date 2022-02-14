from pulp import *

# Descirbe Variables
"""
x1: X veya Y makinesinde üretilen 1.ürün
x2: X makinesinde üretilen 2.ürün
x3: X makinesinde üretilen 3.ürün
x4: X makinesinde üretilen 4.ürün
y2: Y makinesinde üretilen 2.ürün
y3: Y makinesinde üretilen 3.ürün
y4: Y makinesinde üretilen 4.ürün
"""

# 1. Initialize Model
model = LpProblem("max_kar",LpMaximize)

# 2. Define Variables
x1 = LpVariable("x1", lowBound = 0)
x2 = LpVariable("x2", lowBound = 0)
x3 = LpVariable("x3", lowBound = 0)
x4 = LpVariable("x4", lowBound = 0)
y2 = LpVariable("y2", lowBound = 0)
y3 = LpVariable("y3", lowBound = 0)
y4 = LpVariable("y4", lowBound = 0)

# 3. Define Objective Function
model += 10*x1 + 12*(x2 + y2) + 17*(x3 + y3) + 8*(x4 + y4)

# 4. Define Constraints
model += x2 + y2 == 2*(x3 + y3)
model += 10*x1 + 12*x2 + 13*x3 + 8*x4 <= 35*60*0.95
model += 27*x1 + 19*y2 + 33*y3 + 23*y4 <= 35*60*0.93
model += 0.1*x1 + 0.15*(x1 + x2) + 0.5*(x3 + y3) + 0.05*(x4 +y4) <= 50

# 5. Solve Model
model.solve()
print("X veya Y makinesinde üretilen 1.ürün: {}".format(x1.varValue))
print("X makinesinde üretilen 2.ürün {}".format(x2.varValue))
print("X makinesinde üretilen 3.ürün: {}".format(x3.varValue))
print("X makinesinde üretilen 4.ürün {}".format(x4.varValue))
print("Y makinesinde üretilen 2.ürün {}".format(y2.varValue))
print("Y makinesinde üretilen 3.ürün: {}".format(y3.varValue))
print("Y makinesinde üretilen 4.ürün {}".format(y4.varValue))
