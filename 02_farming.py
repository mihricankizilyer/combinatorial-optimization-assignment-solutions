from pulp import *
# Descirbe Variables
"""
x1: Ekilen buğday dönümü
x2: Ekilen mısır dönümü
x3: Ekilen şekerpancarı dönümü
y1: Dışardan satın alınan buğday
y1: Dışardan satın alınan mısır
w1: Satılacak buğday
w2: Satılacak mısır
w3: Yüksek fiyatlı satılacak şeker pancarı
w4: Düşük fiyatlı satılacak şeker pancarı
"""

# 1. Initialize Model
model = LpProblem("min_kar",LpMinimize)

# 2. Define Variables
x1 = LpVariable("x1", lowBound = 0)
x2 = LpVariable("x2", lowBound = 0)
x3 = LpVariable("x3", lowBound = 0)
y1 = LpVariable("y1", lowBound = 0)
y2 = LpVariable("y2", lowBound = 0)
w1 = LpVariable("w1", lowBound = 0)
w2 = LpVariable("w2", lowBound = 0)
w3 = LpVariable("w3", lowBound = 0)
w4 = LpVariable("w4", lowBound = 0)

# 3. Define Objective Function
model += 150*x1 + 230*x2 + 260*x3 + 238*y1 + 210*y2 - 170*w1 - 150*w2 - 36*w3 - 10*w4

# 4. Define Constraints
model += x1 + x2 + x3 <= 500
model += 2.5*x1 + y1 - w1 >= 200
model += 3*x2 + y2 -w2 >= 240
model += w3 <= 6000
model += w3 + w4 <= 20*x3

# 5. Solve Model
model.solve()
print("Ekilen buğday dönümü: {}".format(x1.varValue))
print("Ekilen mısır dönümü {}".format(x2.varValue))
print("Ekilen şekerpancarı dönümü: {}".format(x3.varValue))
print("Dışardan satın alınan buğday {}".format(y1.varValue))
print("Dışardan satın alınan mısır: {}".format(y2.varValue))
print("Satılacak buğday: {}".format(w1.varValue))
print("Satılacak mısır {}".format(w2.varValue))
print("Yüksek fiyatlı satılacak şeker pancarı: {}".format(w3.varValue))
print("Düşük fiyatlı satılacak şeker pancarı: {}".format(w4.varValue))
