# import libraries
import numpy as np
import pandas as pd
from pulp import *

# Decision Variables
# x: light süt miktarı
# y: normal süt miktarı

# 1. Initialize Model
model = LpProblem("max_kar",LpMaximize)

# 2. Define Variables
o = LpVariable("o", lowBound = 1)
n = LpVariable("n", lowBound = 0)
e = LpVariable("e", lowBound = 1)
t = LpVariable("t", lowBound = 1)
w = LpVariable("w", lowBound = 0)
h = LpVariable("h", lowBound = 0)
r = LpVariable("r", lowBound = 0)
l = LpVariable("l", lowBound = 0)
v = LpVariable("v", lowBound = 0)
y = LpVariable("y", lowBound = 0)
M = 200

# 3. Define Objective Function
model += x

# 4. Define Constraints
model += 3 * e + 2 * o + n == y
model += 2 * n + 2 * w + 2 * e == t
model += 2 * o + 2 * t + r + v == n
model += h + e == e
model += t + l == w
model += e == t


# 5.Solve Model
model.solve()
print("Light Süt Miktarı {}".format(x.varValue))
print("Normal Süt Miktarı {}".format(y.varValue))


