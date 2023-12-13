import sys
sys.path.insert(0, '../..')
from utils import *

from functools import reduce
from collections import defaultdict, Counter
import itertools
import re


def q(file):
    #Input -> List<List<complex number>>
    lines = open(file, 'r').read().strip()
    lists = [[curr_col + curr_row * 1j for curr_row, l in enumerate(group.split('\n')) for curr_col, x in enumerate(l) if x == '#'] for group in lines.split('\n\n')]

    tot1 = tot2 = 0
    for ind, l in enumerate(lists):
        max_col = max([int(x.real) for x in l])
        for col in range(1, max_col+1):
            fails = 0

            for i in l:
                check = i + (col - i.real) * 2 - 1
                if check.real > max_col or check.real < 0 or check in l:
                    continue
                else:
                    fails += 1

            if fails == 1:
                tot2 += col
            elif fails == 0:
                tot1 += col
            found = False
            fails = 0

        max_row = max([int(x.imag) for x in l])
        for row in range(1, max_row+1):
            fails = 0

            for i in l:
                check = i + (row - i.imag) * 2j - 1j
                if check.imag > max_row or check.imag < 0 or check in l:
                    continue
                else:
                    fails += 1

            if fails == 1:
                tot2 += row * 100
            elif fails == 0:
                tot1 += row * 100
            found = False
            fails = 0
        
    return (tot1, tot2)

if __name__ == "__main__":
    print('Question (1,2)')
    file = 'test.txt'
    ans(q(file), 'test', copy=False)
    file = 'input.txt'
    ans(q(file), 'input', copy=True)