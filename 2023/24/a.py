import sys
sys.path.insert(0, '../..')
from utils import *

from functools import reduce
from collections import defaultdict, Counter
import itertools
import math
import heapq #heappush heappop
import re

def sign(x):
    return 1 if x > 0 else -1 if x < 0 else 0

import sympy as sp
def q(file):
    lines = [l for l in open(file, 'r')]

    hail = []
    eqs = []

    i=0
    hx, hy, hz, hdx, hdy, hdz = sp.symbols('hx, hy, hz, hdx, hdy, hdz')
    for l in lines:
        i += 1
        l = l.strip()
        x,y,z,dx,dy,dz = ints(l)
        slope = dy/dx
        b = y - slope * x
        hail.append([b, slope, [x,y,z,dx,dy,dz]])

        if i < 4: #First 3 points are enough for this problem
            T = sp.symbols('T' + str(i))
            eqs.append(sp.Eq(x + dx * T, hx + hdx * T))
            eqs.append(sp.Eq(y + dy * T, hy + hdy * T))
            eqs.append(sp.Eq(z + dz * T, hz + hdz * T))
    
    #Just throw it in a solver...
    ans = sp.solve(set(eqs))
    q1 = ans[0][hx] + ans[0][hy] + ans[0][hz]

    q2 = 0
    for (c,a,i1),(d,b,i2) in itertools.combinations(hail, 2):
        if a-b == 0:
            continue
        x = (d-c)/(a-b)
        y = a*((d-c)/(a-b))+c
        
        h1_time = (y-i1[1])/i1[4]
        h2_time = (y-i2[1])/i2[4]

        if 200000000000000 <= x <= 400000000000000 and 200000000000000 <= y <= 400000000000000 and h1_time >= 0 and h2_time >= 0:
            q2 += 1
        
    return q1, q2

if __name__ == "__main__":
    print('Question 1,2 (only for input.txt):')
    file = 'input.txt'
    ans(q(file), 'input', copy=True)