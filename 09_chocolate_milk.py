from pulp import *

# Descirbe Variables
"""
x11: 1.bölümde 1.ürünün işlenme miktarı
x21: 2.bölümde 1.ürünün işlenme miktarı
x12: 1.bölümde 2.ürünün işlenme miktarı
x22: 2.bölümde 2.ürünün işlenme miktarı
x13: 1.bölümde 3.ürünün işlenme miktarı
x23: 2.bölümde 3.ürünün işlenme miktarı
y: elimde bulunan sütlü çikolata miktarı
"""

# 1. Initialize Model
model = LpProblem("max_kar",LpMaximize)

# 2. Define Variables
x11 = LpVariable("x11", lowBound = 0)
x21 = LpVariable("x21", lowBound = 0)
x12 = LpVariable("x12", lowBound = 0)
x22 = LpVariable("x22", lowBound = 0)
x13 = LpVariable("x13", lowBound = 0)
x23 = LpVariable("x23", lowBound = 0)
y = LpVariable("y", lowBound = 0)


# 3. Define Objective Function
model += y

# 4. Define Constraints
model += 0.4*x11 + 0.3*x12 + 0.5*x13 <= 150
model += 0.6*x21 + 0.2*x22 + 0.6*x23 <= 150
model += x11 + x21 >= y*0.5
model += x12 + x22 >= y*0.4
model += x13 + x23 >= y*0.1


# 5. Solve Model
model.solve()
print("1.bölümde 1.ürünün işlenme miktarı: {}".format(x11.varValue))
print("2.bölümde 1.ürünün işlenme miktarı {}".format(x21.varValue))
print("1.bölümde 2.ürünün işlenme miktarı: {}".format(x12.varValue))
print("2.bölümde 2.ürünün işlenme miktarı {}".format(x22.varValue))
print("1.bölümde 3.ürünün işlenme miktarı {}".format(x13.varValue))
print("2.bölümde 3.ürünün işlenme miktarı: {}".format(x23.varValue))
print("Sütlü çikolata miktarı {}".format(y.varValue))
