from pulp import *
# Descirbe Variables
"""
x1: Normal mesainin 1.periyottaki üretim miktarı
x2: Normal mesainin 2.periyottaki üretim miktarı
x3: Normal mesainin 3.periyottaki üretim miktarı
x4: Normal mesainin 4.periyottaki üretim miktarı
y1: Fazla mesainin 1.periyottaki üretim miktarı
y2: Fazla mesainin 2.periyottaki üretim miktarı
y3: Fazla mesainin 3.periyottaki üretim miktarı
y4: Fazla mesainin 4.periyottaki üretim miktarı
z0: 0.dönemden sonraki döneme taşınan miktar
z1: 1.dönemden sonraki döneme taşınan miktar
z2: 2.dönemden sonraki döneme taşınan miktar
z3: 3.dönemden sonraki döneme taşınan miktar
z4: 4.dönemden sonraki döneme taşınan miktar
"""
# 1. Initialize Model
model = LpProblem("min",LpMinimize)

# 2. Define Variables
x1 = LpVariable("x1", lowBound = 0)
x2 = LpVariable("x2", lowBound = 0)
x3 = LpVariable("x3", lowBound = 0)
x4 = LpVariable("x4", lowBound = 0)
y1 = LpVariable("y1", lowBound = 0)
y2 = LpVariable("y2", lowBound = 0)
y3 = LpVariable("y3", lowBound = 0)
y4 = LpVariable("y4", lowBound = 0)
z0 = LpVariable("z0", lowBound = 15, upBound = 15)
z1 = LpVariable("z1", lowBound = 0)
z2 = LpVariable("z2", lowBound = 0)
z3 = LpVariable("z3", lowBound = 0)
z4 = LpVariable("z4", lowBound = 0)

# 3. Define Objective Function
model += 6*x1 + 4*x2 + 8*x3 + 9*x4 + 8*y1 + 6*y2 + 10*y3 + 11*y4 \
    + 1.5*(z0 + z1 + z2 + z3 + z4)

# 4. Define Constraints
model += x1 <= 100
model += x2 <= 100
model += x3 <= 100
model += x4 <= 100
model += y1 <= 60
model += y2 <= 65
model += y3 <= 70
model += y4 <= 60
model += z0 == 15

model += 70 >= z0
model += 70 >= z1
model += 70 >= z2
model += 70 >= z3
model += 70 >= z4

model += z0 + x1 + y1 - 130 == z1
model += z1 + x2 + y2 - 80 == z2
model += z2 + x3 + y3 - 125 == z3
model += z3 + x4 + y4 - 195 == z4

model += z0 + x1 + y1 >= 130
model += z1 + x2 + y2 >= 80
model += z2 + x3 + y3 >= 125
model += z3 + x4 + y4 >= 195

# 5. Solve Model
model.solve()
print("Normal mesainin 1.periyottaki üretim miktarı: {}".format(x1.varValue))
print("Normal mesainin 2.periyottaki üretim miktarı: {}".format(x2.varValue))
print("Normal mesainin 3.periyottaki üretim miktarı: {}".format(x3.varValue))
print("Normal mesainin 4.periyottaki üretim miktarı: {}".format(x4.varValue))

print("Fazla mesainin 1.periyottaki üretim miktarı: {}".format(y1.varValue))
print("Fazla mesainin 2.periyottaki üretim miktarı: {}".format(y2.varValue))
print("Fazla mesainin 3.periyottaki üretim miktarı: {}".format(y3.varValue))
print("Fazla mesainin 4.periyottaki üretim miktarı: {}".format(y4.varValue))

print("0.dönemden sonraki döneme taşınan miktar: {}".format(z0.varValue))
print("1.dönemden sonraki döneme taşınan miktar: {}".format(z1.varValue))
print("2.dönemden sonraki döneme taşınan miktar: {}".format(z2.varValue))
print("3.dönemden sonraki döneme taşınan miktar: {}".format(z3.varValue))
print("4.dönemden sonraki döneme taşınan miktar: {}".format(z4.varValue))
