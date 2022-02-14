from pulp import *

# Descirbe Variables
# 1. Initialize Model
model = LpProblem("min",LpMinimize)

# 2. Define Variables
x1 = LpVariable("x1", lowBound = 0, cat = "Binary")
x2 = LpVariable("x2", lowBound = 0, cat = "Binary")
x3 = LpVariable("x3", lowBound = 0, cat = "Binary")
x4 = LpVariable("x4", lowBound = 0, cat = "Binary")
x5 = LpVariable("x5", lowBound = 0, cat = "Binary")
x6 = LpVariable("x6", lowBound = 0, cat = "Binary")

# 3. Define Objective Function
model += x1 +x2 +x3 +x4 + x5 +x6

# 4. Define Constraints
model += x1 + x3 + x5 >= 1
model += x2 + x4 + x6 >= 1
model += x3 + x1 >= 1
model += x4 + x2 >= 1
model += x5 + x1 + x6 >= 1
model += x6 + x2 + x5 >= 1

# 5. Solve Model
model.solve()
print("1.bölgede servis olacaksa 1 yaz olmayacaksa 0: {}".format(x1.varValue))
print("2.bölgede servis olacaksa 1 yaz olmayacaksa 0: {}".format(x2.varValue))
print("3.bölgede servis olacaksa 1 yaz olmayacaksa 0: {}".format(x3.varValue))
print("4.bölgede servis olacaksa 1 yaz olmayacaksa 0: {}".format(x4.varValue))
print("5.bölgede servis olacaksa 1 yaz olmayacaksa 0: {}".format(x5.varValue))
print("6.bölgede servis olacaksa 1 yaz olmayacaksa 0: {}".format(x6.varValue))
