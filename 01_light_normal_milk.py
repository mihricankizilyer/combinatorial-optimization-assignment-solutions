import numpy as np
import pandas as pd

# !pip install pulp
# x: light süt miktarı
# y: normal süt miktarı

from pulp import *

# 1. Initialize Model
model = LpProblem("max_kar",LpMaximize)

# 2. Define Variables
x = LpVariable("x", lowBound = 0, cat = "Integer")
y = LpVariable("y", lowBound = 0, cat = "Integer")

# 3. Define Objective Function
model += 2.5 * x + 1.5 * y

# 4. Define Constraints
model +=  3 * x + 2 * y <= 12
model += x + 2 * y <= 6

# 5.solve Model
model.solve()
print("Light Süt Miktarı {}".format(x.varValue))
print("Normal Süt Miktarı {}".format(y.varValue))


