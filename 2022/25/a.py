import sys
sys.path.insert(0, '../..')
from utils import lmap, ints, strs, ans

import itertools
import re
from math import *

vals = list('=-012')

def std(s):
    tot = 0
    mult = 1
    for c in s[::-1]:
        tot += mult * (vals.index(c) - 2)
        mult *= 5

    return tot

def dts(tot):
    snafu = ''
    mult = 1
    
    while tot > 0:
        c = int((tot / mult) % 5)
        snafu += vals[(c + 2)%5]

        if c >= 3:
            c -= 5
        tot -= int(mult) * c

        mult *= 5
    return snafu[::-1]

def q(file):
    tot = 0 
    for l in open(file, 'r').readlines():
        l = l.strip()
        tot += std(l)
        
    return dts(tot)

if __name__ == "__main__":
    file = 'test.txt'
    ans(q(file), 'test', copy=False)
    file = 'input.txt'
    ans(q(file), 'input', copy=True)