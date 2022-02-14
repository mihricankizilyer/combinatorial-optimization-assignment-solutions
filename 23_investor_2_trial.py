# import libraries
from pulp import *

# Decision Variables
"""
x1: 1.projeye yatırılım yapılırsa (1 veya 0)
x2: 2.projeye yatırılım yapılırsa (1 veya 0)
x3: 3.projeye yatırılım yapılırsa (1 veya 0)
x4: 4.projeye yatırılım yapılırsa (1 veya 0)
x5: 5.projeye yatırılım yapılırsa (1 veya 0)
x6: 6.projeye yatırılım yapılırsa (1 veya 0)
x7: 7.projeye yatırılım yapılırsa (1 veya 0)
x8: 8.projeye yatırılım yapılırsa (1 veya 0)
x9: 9.projeye yatırılım yapılırsa (1 veya 0)
x10: 10.projeye yatırılım yapılırsa (1 veya 0)
"""

# 1. Initialize Model
model = LpProblem("max_kar",LpMaximize)
# 2. Define Variables
x1 = LpVariable("x1", lowBound = 0, cat = "Binary")
x2 = LpVariable("x2", lowBound = 0, cat = "Binary")
x3 = LpVariable("x3", lowBound = 0, cat = "Binary")
x4 = LpVariable("x4", lowBound = 0, cat = "Binary")
x5 = LpVariable("x5", lowBound = 0, cat = "Binary")
x6 = LpVariable("x6", lowBound = 0, cat = "Binary")
x7 = LpVariable("x7", lowBound = 0, cat = "Binary")
x8 = LpVariable("x8", lowBound = 0, cat = "Binary")
x9 = LpVariable("x9", lowBound = 0, cat = "Binary")
x10 = LpVariable("x10", lowBound = 0, cat = "Binary")
y = LpVariable("y", lowBound = 0, cat = "Binary")
# 3. Define Objective Function
model += 1 * x1 + 2 * x2 + 3 * x3 + 4 * x4 + 5 * x5 + 6 * x6 + 7 * x7 + 8 * x8 + 9 * x9 + 10 * x10
# 4. Define Constraints
model +=  x1 + 2*x2 + 3*x3 + 4*x4 + 5*x5 + 6*x6 + 7*x7 + 8*x8 + 9*x9 + 10*x10 <=300
model +=  x1 + 2*x2 + 3*x3 + 4*x4 + 5*x5 + 6*x6 + 7*x7 + 8*x8 + 9*x9 + 10*x10 <=300
model += x1 + x2 + x3 >= 2 * y
model += x4 + x5 + x6 + x7 + x8 >= 2 * (y-1)
# 5.Solve Model
model.solve()



