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
x = LpVariable("x", lowBound = 0)
y = LpVariable("y", lowBound = 0)

# 3. Define Objective Function
model += 2.5 * x + 1.5 * y

# 4. Define Constraints
model +=  3 * x + 2 * y <= 720
model += x + 2 * y <= 360

# 5.Solve Model
model.solve()
print("Light Süt Miktarı {}".format(x.varValue))
print("Normal Süt Miktarı {}".format(y.varValue))


