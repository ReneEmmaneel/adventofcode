import sys
sys.path.insert(0, '../..')
from utils import *

from functools import reduce
from collections import defaultdict
import itertools
import re


def cmp(l, r):
    if l == r:
        return 0

    if type(l) == int and type(r) == int:
        return -1 if l < r else 1
    
    if type(l) == list and type(r) == list:
        if len(l) == 0 and len(r) == 0:
            return 0
        if len(l) == 0:
            return -1
        if len(r) == 0:
            return 1
        
        a = cmp(l[0], r[0])
        return cmp(l[1:], r[1:]) if a == 0 else a

    if type(l) == int and type(r) == list:
        return cmp([l], r)
    
    if type(l) == list and type(r) == int:
        return cmp(l, [r])

def q(file):
    lines = [l for l in open(file, 'r').readlines()]
    tot = 0 
    q1 = 0

    packets = []

    for i in range(0, len(lines), 3):
        packets.append(eval(lines[i]))
        packets.append(eval(lines[i+1]))

        if cmp(*packets[-2:]) == -1:
            q1 += i // 3 + 1
        
    #Calculate q2
    i1, i2 = 0,0
    for i in packets:
        i1 += (cmp([[2]], i)) / 2 + .5 
        i2 += (cmp([[6]], i)) / 2 + .5
    
    i1 += 1
    i2 += 2
    q2 = int(i1 * i2)

    return q1, q2

if __name__ == "__main__":
    file = 'test.txt'
    ans(q(file), 'test', copy=False)
    file = 'input.txt'
    ans(q(file), 'input', copy=True)