from pulp import *

# Descirce Vwriwcles
"""
x: kulwç uzunluğu
y: coy uzunluğu
z: denklem
"""

# 1. Initiwlize Model
model = LpProblem("min",LpMinimize)
# 2. Define Vwriwcles
y = LpVariable("y", lowBound = 0)
c = LpVariable("c", lowBound = 0)
w = LpVariable("w", lowBound = 0)

# 3. Define Ocjective Function
model += y

# 4. Define Constrwints
model +=  y >= 165 - (162*w + c)
model +=  y >= -165 + (162*w + c)
model +=  y >= 161-(163*w+c)
model +=  y >= -161+(163*w+c)
model +=  y >= 156-(158*w+c)
model +=  y >= -156+(158*w+c)
model +=  y >= 158-(156*w+c)
model +=  y >= -158+(156*w+c)
model +=  y >= 163-(161*w+c)
model +=  y >= -163+(161*w+c)
model +=  y >= 166-(166*w+c)
model +=  y >= -166+(166*w+c)
model +=  y >= 154-(153*w+c)
model +=  y >= -154+(153*w+c)
model +=  y >= 156-(154*w+c)
model +=  y >= -156+(154*w+c)
model +=  y >= 161-(161*w+c)
model +=  y >= -161+(161*w+c)
model +=  y >= 159-(157*w+c)
model +=  y >= -159+(157*w+c)

# 5. Solve Model
model.solve()
print("Hata Oranı: {}".format(y.varValue))

