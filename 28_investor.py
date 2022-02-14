from pulp import *

# 1. Initialize Model
model = LpProblem("max",LpMaximize)

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

# 3. Define Objective Function
model += x1 + x2 + x3 + x4 + x5 + x6 + x7

# 4. Define Constraints
model += x1 + x3 + x4 + x5 +x6 + x7 >= 8
model += x1 + x2 + x4 + x5 +x6 + x7 >= 6
model += x1 + x2 + x3 + x5 +x6 + x7 >= 7
model += x1 + x2 + x3 + x4 +x6 + x7 >= 6
model += x1 + x2 + x3 + x4 +x5 + x7 >= 9
model += x1 + x2 + x3 + x4 +x5 + x6 >= 11
model += x2 + x3 + x4 + x5 +x6 + x7 >= 9

# 5. Solve Model
model.solve()
print("1.günde başlayan eleman sayısı: {}".format(x1.varValue))
print("2.günde başlayan eleman sayısı: {}".format(x2.varValue))
print("3.günde başlayan eleman sayısı: {}".format(x3.varValue))
print("4.günde başlayan eleman sayısı: {}".format(x4.varValue))
print("5.günde başlayan eleman sayısı: {}".format(x5.varValue))
print("6.günde başlayan eleman sayısı: {}".format(x6.varValue))
print("7.günde başlayan eleman sayısı: {}".format(x7.varValue))
