from pulp import *
# Descirbe Variables
"""
x1: 1.ürünün pozitif yönde sapma miktarı
x2: 1.ürünün negatif yönde sapma miktarı
x3: 2.ürünün pozitif yönde sapma miktarı
x4: 2.ürünün negatif yönde sapma miktarı
"""
# 1. Initialize Model
model = LpProblem("min",LpMinimize)
# 2. Define Variables
x1 = LpVariable("x1", lowBound = 0)
x2 = LpVariable("x2", lowBound = 0)
x3 = LpVariable("x3", lowBound = 0)
x4 = LpVariable("x4", lowBound = 0)
# 3. Define Objective Function
model += 50*(x1 + x2) + 45*(x3 + x4)
# 4. Define Constraints
model += (3.2) *(100 + x1 - x2) + 2*(90 + x3 - x4) <= 480
# 5. Solve Model
model.solve()
print("1.ürünün pozitif yönde sapma miktarı: {}".format(x1.varValue))
print("1.ürünün negatif yönde sapma miktarı: {}".format(x2.varValue))
print("2.ürünün pozitif yönde sapma miktarı: {}".format(x3.varValue))
print("1.ürünün negatif yönde sapma miktarı: {}".format(x4.varValue))

