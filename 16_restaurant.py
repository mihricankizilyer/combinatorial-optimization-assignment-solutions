from pulp import *

# Descirbe Variables
"""
x1: 1.günde başlayan eleman sayısı
x2: 2.günde başlayan eleman sayısı
x3: 3.günde başlayan eleman sayısı
x4: 4.günde başlayan eleman sayısı
x5: 5.günde başlayan eleman sayısı
x6: 6.günde başlayan eleman sayısı
x7: 7.günde başlayan eleman sayısı
"""

# 1. Initialize Model
model = LpProblem("min",LpMinimize)

# 2. Define Variables
x1 = LpVariable("x1", lowBound = 0, cat = "Integer")
x2 = LpVariable("x2", lowBound = 0, cat = "Integer")
x3 = LpVariable("x3", lowBound = 0, cat = "Integer")
x4 = LpVariable("x4", lowBound = 0, cat = "Integer")
x5 = LpVariable("x5", lowBound = 0, cat = "Integer")
x6 = LpVariable("x6", lowBound = 0, cat = "Integer")
x7 = LpVariable("x7", lowBound = 0, cat = "Integer")


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
