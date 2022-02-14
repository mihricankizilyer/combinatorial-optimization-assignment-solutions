from pulp import *
# Descirbe Variables
"""
y12011 = 1.seçenektem 2011 yılına
y12012 = 1.seçenekten 2012 yılına
y22011 = 2.seçenekten 2011 yılına
y22012 = 2.seçenekten 2012 yılına
y22013 = 2.seçenekten 2013 yılına
y32011 = 3.seçenekten 2011 yılına
y42012 = 4.seçenekten 2012 yılına
x0 = 2011 yılının başında elimizde olan miktar
x1 = 2012 yılının başında elimizde olan miktar
x2 = 2013 yılının başında elimizde olan miktar
x3 = 2014 yılının başında elimizde olan miktar
"""
# 1. Initialize Model
model = LpProblem("max_kar",LpMaximize)
# 2. Define Variables
y12011 = LpVariable("y12011", lowBound = 0)
y12012 = LpVariable("y12012", lowBound = 0)
y22011 = LpVariable("y22011", lowBound = 0)
y22012 = LpVariable("y22012", lowBound = 0)
y22013 = LpVariable("y22013", lowBound = 0)
y32011 = LpVariable("y32011", lowBound = 0)
y42012 = LpVariable("y42012", lowBound = 0)
x0 = LpVariable("x0", lowBound = 0)
x1 = LpVariable("x1", lowBound = 0)
x2 = LpVariable("x2", lowBound = 0)
x3 = LpVariable("x3", lowBound = 0)


# 3. Define Objective Function
model += x3

# 4. Define Constraints
model += x0 == 10000
model += x2 == y22013
model += x0 == y12011 + y22011 + y32011
model += x1 == 1.12 * y22011
model += x1 == y12012 + y22012 + y42012
model += x2 == 1.26 * y12011 + 1.12 * y22012
model += x3 == 1.38 * y32011 + 1.12 * y22013 + 1.26 * y12012 + 1.27 * y42012

# 5. Solve Model
model.solve()
print("1.seçenektem 2011 yılına: {}".format(y12011.varValue))
print("1.seçenekten 2012 yılına {}".format(y12012.varValue))
print("2.seçenekten 2011 yılına: {}".format(y22011.varValue))
print("2.seçenekten 2012 yılına {}".format(y22012.varValue))
print("2.seçenekten 2013 yılına: {}".format(y22013.varValue))
print("3.seçenekten 2011 yılına: {}".format(y32011.varValue))
print("4.seçenekten 2012 yılına: {}".format(y42012.varValue))
print("2011 yılının başında elimizde olan miktar: {}".format(x0.varValue))
print("2012 yılının başında elimizde olan miktar: {}".format(x1.varValue))
print("2013 yılının başında elimizde olan miktar: {}".format(x2.varValue))
print("2014 yılının başında elimizde olan miktar: {}".format(x3.varValue))

