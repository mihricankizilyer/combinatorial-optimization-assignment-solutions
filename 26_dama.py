from pulp import *

# 1. Initialize Model
model = LpProblem("max",LpMaximize)

# 2. Define Variables
y1 = LpVariable("y1", lowBound = 0, cat = "Binary")
y2 = LpVariable("y2", lowBound = 0, cat = "Binary")
y3 = LpVariable("y3", lowBound = 0, cat = "Binary")
y4 = LpVariable("y4", lowBound = 0, cat = "Binary")
y5 = LpVariable("y5", lowBound = 0, cat = "Binary")
y6 = LpVariable("y6", lowBound = 0, cat = "Binary")
y7 = LpVariable("y7", lowBound = 0, cat = "Binary")
y8 = LpVariable("y8", lowBound = 0, cat = "Binary")
y9 = LpVariable("y9", lowBound = 0, cat = "Binary")
y10 = LpVariable("y10", lowBound = 0, cat = "Binary")
y11 = LpVariable("y11", lowBound = 0, cat = "Binary")
y12 = LpVariable("y12", lowBound = 0, cat = "Binary")
y13 = LpVariable("y13", lowBound = 0, cat = "Binary")
y14 = LpVariable("y14", lowBound = 0, cat = "Binary")
y15 = LpVariable("y15", lowBound = 0, cat = "Binary")
y16 = LpVariable("y16", lowBound = 0, cat = "Binary")

x11 = LpVariable("x11", lowBound = 0, cat = "Binary")
x12 = LpVariable("x12", lowBound = 0, cat = "Binary")
x13 = LpVariable("x13", lowBound = 0, cat = "Binary")
x14 = LpVariable("x14", lowBound = 0, cat = "Binary")
x21 = LpVariable("x21", lowBound = 0, cat = "Binary")
x22 = LpVariable("x22", lowBound = 0, cat = "Binary")
x23 = LpVariable("x23", lowBound = 0, cat = "Binary")
x24 = LpVariable("x24", lowBound = 0, cat = "Binary")
x31 = LpVariable("x31", lowBound = 0, cat = "Binary")
x32 = LpVariable("x32", lowBound = 0, cat = "Binary")
x33 = LpVariable("x33", lowBound = 0, cat = "Binary")
x34 = LpVariable("x34", lowBound = 0, cat = "Binary")
x41 = LpVariable("x41", lowBound = 0, cat = "Binary")
x42 = LpVariable("x42", lowBound = 0, cat = "Binary")
x43 = LpVariable("x43", lowBound = 0, cat = "Binary")
x44 = LpVariable("x44", lowBound = 0, cat = "Binary")


# 3. Define Objective Function
model += x11 +x12 +x13 +x14 +x21 +x22 +x23 +x24 +x31 +x32 +x34 +x41 +x42 +x43 +x44

# 4. Define Constraints
model += x11 + x12 + x13 + x14 == 2 * y1 + 4*y2
model += y1 + y2 == 1
model += x21 + x22 + x23 + x24 == 2*y3 + 4*y4
model += y3 + y4 == 1
model += x31 + x32 + x33 + x34 == 2*y5 + 4*y6
model += y5 + y6 == 1
model += x41 + x42 + x43 + x44 == 2*y7 + 4*y8
model += y7 - y8 == 1
model += x11 + x12 + x13 + x14 + x21 + x22 + x23 + x24 + x31 + x32 + x33 - x34 + x41 + x42 - x43 + x44 == 10



# 5. Solve Model
model.solve()
print("y1: {}".format(y1.varValue))
print("y2: {}".format(y2.varValue))
print("y3: {}".format(y3.varValue))
print("y4: {}".format(y4.varValue))
print("y5: {}".format(y5.varValue))
print("y6: {}".format(y6.varValue))
print("y7: {}".format(y7.varValue))
print("y8: {}".format(y8.varValue))

print("x11: {}".format(x11.varValue))
print("x12: {}".format(x12.varValue))
print("x13: {}".format(x13.varValue))
print("x14: {}".format(x14.varValue))
print("x21: {}".format(x21.varValue))
print("x22: {}".format(x22.varValue))
print("x23: {}".format(x23.varValue))
print("x24: {}".format(x24.varValue))
print("x31: {}".format(x31.varValue))
print("x32: {}".format(x32.varValue))
print("x33: {}".format(x33.varValue))
print("x34: {}".format(x34.varValue))
print("x41: {}".format(x41.varValue))
print("x42: {}".format(x42.varValue))
print("x43: {}".format(x43.varValue))
print("x44: {}".format(x44.varValue))