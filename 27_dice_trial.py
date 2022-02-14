from pulp import *

# 1. Initialize Model
model = LpProblem("max",LpMaximize)

i = [0,1,2,3,4]
j = [0,1,2,3,4]
k = range(16)

for m in range(len(i)):
    for n in range(len(j)):
        print([m,n])