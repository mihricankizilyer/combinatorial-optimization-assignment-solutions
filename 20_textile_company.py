# import libraries
import numpy as np
import pandas as pd
from pulp import *

# Decision Variables
"""
x1: üretilen tişört miktarı
x2: üretilen şort miktarı
x3: üretilen pantolon miktarı
"""

# 1. Initialize Model
model = LpProblem("max_kar",LpMaximize)

# 2. Define Variables
x1 = LpVariable("x1", lowBound = 0)
x2 = LpVariable("x2", lowBound = 0)
x3 = LpVariable("x3", lowBound = 0)
y1 = LpVariable("y1", lowBound = 1, cat = "Binary")
y2 = LpVariable("y2", lowBound = 0, cat = "Binary")
y3 = LpVariable("y3", lowBound = 0, cat = "Binary")
M = 2000

# 3. Define Objective Function
model += 6*x1 + 4*x2 + 7*x3 - 200*y1 - 150*y2 - 100*y3

# 4. Define Constraints
model +=  3*x1 + 2*x2 + 6*x3 <= 150
model +=  4*x1 + 3*x2 + 4*x3 <= 160
model += x1 <= M * y1
model += x2 <= M * y2
model += x3 <= M * y3

# 5.Solve Model
model.solve()
print("Üretilecek Tişört Miktarı: {}".format(x1.varValue))
print("Üretilecek Şort Miktarı: {}".format(x2.varValue))
print("Üretilecek Pantolon Miktarı: {}".format(x3.varValue))

