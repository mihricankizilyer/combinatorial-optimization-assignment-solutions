from pulp import *

# Descirbe Variables
"""
x1: 1.ürünün üretim miktarı
x2: 2.ürünün üretim miktarı
x3: 3.ürünün üretim miktarı
x4: 4.ürünün üretim miktarı
tba: B'dan A'ya aktarılan zaman
tca: C'den A'ya aktarılan zaman
"""

# 1. Initialize Model
model = LpProblem("max_kar",LpMaximize)

# 2. Define Variables
x1 = LpVariable("x1", lowBound = 0)
x2 = LpVariable("x2", lowBound = 0)
x3 = LpVariable("x3", lowBound = 0)
x4 = LpVariable("x4", lowBound = 0)
tba = LpVariable("tba", lowBound = 0)
tca = LpVariable("tca", lowBound = 0)

# 3. Define Objective Function
model += 10*x1 + 15*x2 + 22*x3 + 17*x4

# 4. Define Constraints
model += 2*x1 + 2*x2 + x3 + x4 <= 160 + tba + tca
model += 2*x1 + 4*x2 + x3 + 2*x4 <= 200 - tba
model += 3*x1 + 6*x2 + x3 + 5*x4 <= 80 - tca
model += x1 <= 1.15*x4
model += x1 >= 0.9*x4
model += tba <= 40
model += tca <= 24
model += x1 <= 50
model += x2 <= 60
model += x3 <= 85
model += x4 <= 70

# 5. Solve Model
model.solve()
print("1.ürünün üretim miktarı: {}".format(x1.varValue))
print("2.ürünün üretim miktarı {}".format(x2.varValue))
print("3.ürünün üretim miktarı: {}".format(x3.varValue))
print("4.ürünün üretim miktarı {}".format(x4.varValue))
print("B'dan A'ya aktarılan zaman {}".format(tba.varValue))
print("C'den A'ya aktarılan zaman: {}".format(tca.varValue))
