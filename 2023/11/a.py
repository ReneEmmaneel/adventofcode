import sys
sys.path.insert(0, '../..')
from utils import *

from functools import reduce
from collections import defaultdict, Counter
import itertools
import re


def q(file, q2):
    lines = [l for l in open(file, 'r')]

    gal = [x+y*1j for y, line in enumerate(lines) for x, v in enumerate(line) if v == '#' ]

    em_rows = set(list(range(len(lines)))) - set([int(x.real) for x in gal])
    em_cols = set(list(range(len(lines)))) - set([int(x.imag) for x in gal])
    
    dists = []
    for a, b in itertools.combinations(gal,2):
        dist = abs(a.real - b.real) + abs(a.imag - b.imag) 

        r_betw = list(range(int(min(a.real, b.real)) + 1, int(max(a.real, b.real))))
        c_betw = list(range(int(min(a.imag, b.imag)) + 1, int(max(a.imag, b.imag))))

        em_row_count = len(set(r_betw) & set(em_rows))
        em_col_count  = len(set(c_betw) & set(em_cols))

        mult = 1000000-1 if q2 else 1
        d = dist + em_row_count * mult + em_col_count * mult
        dists.append(d)

    tot = int(sum(dists))

    return tot

if __name__ == "__main__":
    print('Part 1:')
    file = 'test.txt'
    ans(q(file, False), 'test', copy=False)
    file = 'input.txt'
    ans(q(file, False), 'input', copy=True)
    
    print('Part 2:')
    file = 'test.txt'
    ans(q(file, True), 'test', copy=False)
    file = 'input.txt'
    ans(q(file, True), 'input', copy=True)