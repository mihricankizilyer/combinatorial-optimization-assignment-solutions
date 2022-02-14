from pulp import *
import numpy as np
import pandas as pd

data = [(6,10,15,14,16),
        (2,15,12,15,12),
        (3,12,1,15,11)]

işler = ["1","2","3"]
makinalar = ["1","2","3","4","5"]

p = pd.DataFrame(data, columns = makinalar, index= işler)

# 1. Initialize Model
model = LpProblem("min",LpMinimize)

# 2. Create Problem Variables
x11 = LpVariable("x11", lowBound = 0, cat = "Binary")
x12 = LpVariable("x12", lowBound = 0, cat = "Binary")
x13= LpVariable("x13", lowBound = 0, cat = "Binary")
x21= LpVariable("x21", lowBound = 0, cat = "Binary")
x22= LpVariable("x22", lowBound = 0, cat = "Binary")
x23 = LpVariable("x23", lowBound = 0, cat = "Binary")
x31= LpVariable("x31", lowBound = 0, cat = "Binary")
x32= LpVariable("x32", lowBound = 0, cat = "Binary")
x33 = LpVariable("x33", lowBound = 0, cat = "Binary")

st11 = LpVariable("st11", lowBound = 0)
st12 = LpVariable("st12", lowBound = 0)
st13 = LpVariable("st13", lowBound = 0)
st14 = LpVariable("st14", lowBound = 0)
st15 = LpVariable("st15", lowBound = 0)
st21 = LpVariable("st21", lowBound = 0)
st22 = LpVariable("st22", lowBound = 0)
st23 = LpVariable("st23", lowBound = 0)
st24 = LpVariable("st24", lowBound = 0)
st25 = LpVariable("st25", lowBound = 0)
st31 = LpVariable("st31", lowBound = 0)
st32 = LpVariable("st32", lowBound = 0)
st33 = LpVariable("st33", lowBound = 0)
st34 = LpVariable("st34", lowBound = 0)
st35 = LpVariable("st35", lowBound = 0)

# 3. Objective Function
model += st35 + x13*p["5"]["1"] + x23*p["5"]["2"] + x33*p["5"]["3"]


# 4. Define Constraints
model += x11 + x12 + x13 == 1
model += x21 + x22 + x23 == 1
model += x31 + x32 + x33 == 1
model += x11 + x21 + x31 == 1
model += x12 + x22 + x32 == 1
model += x13 + x23 + x33 == 1

# M1 için
model += st21 >= st11 + p["1"]["1"]*x11 + p["1"]["2"]*x21 + p["1"]["3"]*x31
model += st31 >= st21 + p["1"]["1"]*x12 + p["1"]["2"]*x22 + p["1"]["3"]*x32

# M2 için
model += st22 >= st12 + p["2"]["1"]*x11 + p["2"]["2"]*x21 + p["2"]["3"]*x31
model += st32 >= st22 + p["2"]["1"]*x12 + p["2"]["2"]*x23 + p["2"]["3"]*x33

# M3 için
model += st12 >= st11 + p["3"]["1"]*x11 + p["3"]["2"]*x21 + p["3"]["3"]*x31
model += st22 >= st21 + p["3"]["1"]*x12 + p["3"]["2"]*x22 + p["3"]["3"]*x32
model += st32 >= st31 + p["3"]["1"]*x13 + p["3"]["2"]*x23 + p["3"]["3"]*x33

# M4 için
model += st13 >= st11 + p["4"]["1"]*x11 + p["4"]["2"]*x21 + p["4"]["3"]*x31
model += st23 >= st21 + p["4"]["1"]*x12 + p["4"]["2"]*x22 + p["4"]["3"]*x32
model += st33 >= st31 + p["4"]["1"]*x13 + p["4"]["2"]*x23 + p["4"]["3"]*x33

# M5 için
model += st25 >= st15 + p["5"]["1"]*x12 + p["5"]["2"]*x22 + p["5"]["3"]*x32
model += st25 >= st15 + p["5"]["1"]*x12 + p["5"]["2"]*x22 + p["5"]["3"]*x32
model += st35 >= st25 + p["5"]["1"]*x13 + p["5"]["2"]*x23 + p["5"]["3"]*x33

# 5. Solve Model
model.solve()



