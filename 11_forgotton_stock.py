from pulp import *
# Descirbe Variables
"""
P3: 3.aydaki üretim miktarı
P4: 4.aydaki üretim miktarı
P5: 5.aydaki üretim miktarı
P6: 6.aydaki üretim miktarı
P7: 7.aydaki üretim miktarı
P8: 8.aydaki üretim miktarı
P9: 9.aydaki üretim miktarı

I02= 0.ayda üretilen, 2. ayın sonunda stokta olan miktar
I12= 1.ayda üretilen, 2. ayın sonunda stokta olan miktar
I22= 2.ayda üretilen, 2. ayın sonunda stokta olan miktar 
I13= 1.ayda üretilen, 3. ayın sonunda stokta olan miktar
I23= 2.ayda üretilen, 3. ayın sonunda stokta olan miktar
I33= 3.ayda üretilen, 3. ayın sonunda stokta olan miktar

S13 = 1.ayda üretilen 3.ayın başında stokta olan miktar
S23 = 2.ayda üretilen 3.ayın başında stokta olan miktar
S24 = 2.ayda üretilen 4.ayın başında stokta olan miktar
S34 = 3.ayda üretilen 4.ayın başında stokta olan miktar

d13 = 3. ayın talebinin 1. ayın üretiminden kalan miktarı 
d23 = 3. ayın talebinin 2. ayın üretiminden kalan miktarı 
d33 = 3. ayın talebinin 3. ayın üretiminden kalan miktarı 
d24 = 4. ayın talebinin 2. ayın üretiminden kalan miktarı 
d34 = 4. ayın talebinin 3. ayın üretiminden kalan miktarı 
d44 = 4. ayın talebinin 4. ayın üretiminden kalan miktarı 

"""
# 1. Initialize Model
model = LpProblem("min",LpMinimize)

# 2. Define Variables
p3 = LpVariable("p3", lowBound = 0)
p4 = LpVariable("p4", lowBound = 0)
p5 = LpVariable("p5", lowBound = 0)
p6 = LpVariable("p6", lowBound = 0)
p7 = LpVariable("p7", lowBound = 0)
p8 = LpVariable("p8", lowBound = 0)
p9 = LpVariable("p9", lowBound = 0)

I02 = LpVariable("I02", lowBound = 0)
I12 = LpVariable("I12", lowBound = 0)
I22 = LpVariable("I22", lowBound = 0)
I13 = LpVariable("I13", lowBound = 0)
I23 = LpVariable("I23", lowBound = 0)
I33 = LpVariable("I33", lowBound = 0)

s13 = LpVariable("s13", lowBound = 0)
s23 = LpVariable("s23", lowBound = 0)
s234 = LpVariable("s24", lowBound = 0)
s34 = LpVariable("s34", lowBound = 0)

d13 = LpVariable("d13", lowBound = 0)
d23 = LpVariable("d23", lowBound = 0)
d33 = LpVariable("d33", lowBound = 0)
d24 = LpVariable("d24", lowBound = 0)
d34 = LpVariable("d34", lowBound = 0)
d44 = LpVariable("d44", lowBound = 0)




# 3. Define Objective Function
model += 15*(p3+p4+p5+p6+p7+p8+p9) + 0,75*(s23 + s13 + s34 + s24 + s45 + s35 + s)

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
