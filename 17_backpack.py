import pyomo.environ as pyo
from pyomo.environ import *
from pyomo.opt import SolverFactory
import numpy as np
import time

v = {'kalem':8, 'kalemkutu':3, 'saat':6, 'defter':11}
w = {'kalem':5, 'kalemkutu':7, 'saat':4, 'defter':3}

limit = 14

M = ConcreteModel()
M.ITEMS = Set(initialize=v.keys())
M.x = Var(M.ITEMS, within=Binary)

M.value = Objective(expr=sum(v[i]*M.x[i] for i in M.ITEMS), sense=maximize)
M.weight = Constraint(expr=sum(w[i]*M.x[i] for i in M.ITEMS) <= limit)

print('Solved using GLPK')
results = SolverFactory('glpk').solve(M)
print('Objective = ', value(M.value))
results.write()

